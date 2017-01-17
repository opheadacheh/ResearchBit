import os
import sys
import time
import logging
from sets import Set
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def iter_docs(topdir, stoplist):
    for fn in os.listdir(topdir):
        fin = open(os.path.join(topdir, fn), 'rb')
        text = fin.read()
        fin.close()
        yield (x for x in 
            gensim.utils.tokenize(text, lowercase=True, deacc=True, 
                                  errors="ignore")
            if x not in stoplist)

class MyCorpus(object):

    def __init__(self, topdir, stoplist):
        self.topdir = topdir
        self.stoplist = stoplist
        self.dictionary = gensim.corpora.Dictionary(iter_docs(topdir, stoplist))
        
    def __iter__(self):
        for tokens in iter_docs(self.topdir, self.stoplist):
            yield self.dictionary.doc2bow(tokens)


# In[2]:

def readinStopWords():
    with open("../Data/stopwords.txt") as text_file:
        f = text_file.read()
    stops = f.split(" ")
    stop_words_list = stops

    for j in range(len(stop_words_list)):
        stop_words_list[j].decode("utf8")
    stopWords = [unicode(i,encoding='UTF-8') for i in stop_words_list]
    return stopWords


# In[3]:


def readinData():
    df = pd.read_csv("../Data/Data_New/Data_Out/DataFound.csv")
    testdata = df[df['Asilomar'] == True]['Author'].tolist()
    realname = df['Author'].tolist()
    othername = []
    for i in range(len(realname)):
        array = realname[i].lower().split(' ')
        newname = array[0]+array[1]
        newname = newname.replace(' ','')
        othername.append(newname)
    testindex = df[df['Asilomar'] == True]['ID'].tolist()
    return othername,realname,testdata


def readinData2():
    df = pd.read_csv("../Data/AsilomarAttendeeReport.csv")
    realname1 = df['Name'].tolist()
    othername1 = []
    for i in range(173):
        array1 = realname1[i].lower().split(',')
        newname1 = array1[1]+array1[0]
        newname1 = newname1.replace(' ','')
        othername1.append(newname1)
    return othername1,realname1


def build_train_set(topdir, stoplist): 
    train_set = []
    name = []
    for fn in os.listdir(topdir):
        if (fn.find('Compress')!=-1):
            fin = open(os.path.join(topdir, fn), 'rb')
            doc = str.decode(fin.read(), "UTF-8", "ignore")
            train_set.append(doc)
            name.append(fn[fn.find('_')-2:fn.find('Compress')+1])
            fin.close()
    for i in range(len(name)):
        name[i] = name[i][name[i].find('pro')+4:name[i].find('.')]
    return train_set,name



# In[5]:

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)


# In[6]:

def checkMailList(train_set):
    mail = {}
    for i in range(len(train_set)):
        if((train_set[i].find('MailingList')!=-1) & (train_set[i].find('esip-all')==-1)):
            profile = train_set[i]
            position = list(find_all(profile,'ListName'))
            for j in range(0,len(position),2):
                if(mail.has_key(profile[position[j]+9:position[j+1]-2])):
                    mail[profile[position[j]+9:position[j+1]-2]] = mail.get(profile[position[j]+9:position[j+1]-2])+','+str(i)
                else:
                    mail[profile[position[j]+9:position[j+1]-2]] = str(i)
    return mail


# In[7]:

def buildSreModel(basic_matrix,profile,k1,k2,mailingList = False):
    ser_matrix = basic_matrix[:]
    if(mailingList):
        mailMap = checkMailList(profile)
        for mail,people in mailMap.items():
            #print mail,'correspond',people
            array = people.split(',')
            print 'newlist'
            for i in xrange(len(array)):
                print 'target is:',array[i]
                target = int(array[i])
                result = cosine_similarity(basic_matrix[target:target+1], basic_matrix[:])
                for j in array:
                    j = int(j)
                    if(result[0][j]!=1.0):
                        ser_matrix[target] = k1*basic_matrix[target]+sum(basic_matrix[j]*(1/(k2+result[0][j])))
    return ser_matrix


# In[ ]:

def checkCoauther(train_set):
    Coauther = {}
    with open("../Data/Data/IDs_Data/publicationNodes.txt") as text_file:
        f = text_file.read()
    array = f.split('\n')
    for i in xrange(len(array)):
        line = str(array[i]).split(',')
        if((len(line)>2) & (len(line)<10)):
            for j in xrange(len(line)-1):
                key = line[j+1][line[j+1].find('00')+2:]
                key = int(key)
                if(key not in Coauther):
                    Coauther[key] = Set()                      
                for k in xrange(len(line)-1):    
                    num = line[k+1]
                    if (k == len(line)-1):
                        value = num[num.find('00')+2:num.find('\r')]
                    else:
                        value = num[num.find('00')+2:]
                    value = int(value)
                    #print value
                    if((value not in Coauther.get(key)) & (value!=key)):
                        #if(key==0):
                        #    print key,Coauther.get(key)
                        tempset = Coauther.get(key)
                        tempset.add(value)
                        Coauther[key] = tempset
    return Coauther


# In[ ]:

def deleteCoauthor(coauther, recommendation, index):
    flag = True
    originalRec = recommendation[:]
    oriLength = len(recommendation)
    mark = len(recommendation)+1
    while(flag):
        for p in originalRec:
            for q in coauther:
                if(p==q):
                    recommendation.remove(p)
        diff = oriLength - len(recommendation)
        if(diff == 0):
            flag = False
        else:
            newList = index[mark:mark+diff]
            mark = mark + diff
            for value in newList:
                recommendation.append(value)
        originalRec = recommendation[:]   
    return recommendation


# In[64]:

def writeOutput(tfidf_matrix_train,relname,othername,othername1,realname,realname1,authorMap,listsize, outname):
    temp = []
    for j in range(tfidf_matrix_train.shape[0]):
        targetname = relname[j]
        targetname = targetname.strip()
        for n in range(len(othername1)):
            othername1[n] = othername1[n].strip()
            if (targetname == othername1[n]):
                print j,targetname
                temp.append(j)
                #print 'original one'
                result = cosine_similarity(tfidf_matrix_train[j:j+1], tfidf_matrix_train)
                index = [i[0] for i in sorted(enumerate(result[0]), key=lambda x:x[1],reverse=True)]
                recList = index[1:listsize+1]
                if(j in authorMap.keys()):
                    coauther = authorMap.get(j)
                    coauther = list(coauther)
                    recList = deleteCoauthor(coauther, recList, index)
                recomd = []
                similar = []
                for k in recList: 
                    recomd.append(relname[k])
                    similar.append(result[0][k]) 
                with open('../RecommendationResult/'+outname+'Model/'+relname[j]+'.txt','w') as fn:
                    fn.write(realname1[n]+" ID:"+str(j)+"\n\n")
                    for n1 in xrange(len(recomd)):
                        for m in range(len(othername)):
                            person = recomd[n1]
                            person = person.strip()
                            othername[m] = othername[m].strip()
                            if (person == othername[m]):
                                fn.write(str(n1+1)+". "+str(realname[m])+": "+str(similar[n1])+"\n")
    return temp



# if __name__ == "__main__":
def run(k1, k2, listsize, outname):
    start_time = time.time()
    # k1 = int(sys.argv[1])
    # k2 = int(sys.argv[2])
    # listsize = int(sys.argv[3])
    stopWords = readinStopWords()
    train_set,name = build_train_set("../Data/Data/Profile_Data",stopWords)
    tfidf_vectorizer = TfidfVectorizer(norm=u'l2',stop_words=stopWords,use_idf=False)
    basic_profile = tfidf_vectorizer.fit_transform(train_set[:])

    othername,realname,testdata = readinData()
    othername1,realname1 = readinData2()

    ser_profile = buildSreModel(basic_profile,train_set,k1,k2,True)
    authorMap = checkCoauther(train_set)

    writeOutput(ser_profile,name,othername,othername1,realname,realname1,authorMap,listsize, outname)
    print("--- %s seconds ---" % (time.time() - start_time))