
# coding: utf-8

# In[1]:
from __future__ import division
import numpy as np
import logging
import os
import nltk
import gensim
from graphviz import Digraph
from sets import Set

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

with open("../Data/stopwords.txt") as text_file:
    f = text_file.read()
stops = f.split(" ")
stop_words_list = stops

for j in range(len(stop_words_list)):
    stop_words_list[j].decode("utf8")
stopWords = [unicode(i,encoding='UTF-8') for i in stop_words_list]


# In[3]:

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def build_train_set(topdir, stoplist): 
    train_set = []
    name = []
    for fn in os.listdir(topdir):
        if (fn.find('Compress')!=-1):
            fin = open(os.path.join(topdir, fn), 'rb')
            doc = str.decode(fin.read(), "UTF-8", "ignore")
            train_set.append(doc)
            name.append(fn[fn.find('_')+1:fn.find('Compress')])
            fin.close()
    return train_set,name

train_set,name = build_train_set("../Data/Data/Profile_Data",stopWords)

    
tfidf_vectorizer = TfidfVectorizer(norm=u'l2',stop_words=stopWords,use_idf=False)
basic_profile = tfidf_vectorizer.fit_transform(train_set[:])


# In[4]:

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


# In[5]:

authorMap = checkCoauther(train_set)
#print len(authorMap)
#print authorMap.get(481)
#for target,people in authorMap.items():
#    print target,'correspond',people


# In[6]:

import os
import pandas as pd

df = pd.read_csv("../Data/TopicsInDocsNeeded.csv",error_bad_lines=False)

temp1 = df['docId'].tolist()
temp2 = df['filename'].tolist()
temp3 = df['top topics'].tolist()

docid = []
docname = []
doctopic = []
for i in range(len(temp1)):
    name = temp2[i]
    if(name.find('.txt')!=-1):
        did = temp1[i]-2
        name = name[name.find('ATT')+9:name.find('Compressed')]
        docid.append(did)
        docname.append(name)
        doctopic.append(temp3[i])
#print len(docid)
#print len(docname)
#print len(doctopic)
i = 804
#print docid[i]
#print docname[i]
#print doctopic[i]


# In[7]:

import os
import pandas as pd
df = pd.read_csv("../Data/AsilomarAttendeeReport.csv")
realname = df['Name'].tolist()
othername = []
for i in range(173):
    array = realname[i].lower().split(',')
    newname = array[1]+array[0]
    newname = newname.replace(' ','')
    othername.append(newname)
#print othername


# In[8]:

import numpy as np
import logging
import os
from sets import Set

def iter_docs(topdir):
    resultset = []
    nameid = []
    i = 0
    for fn in os.listdir(topdir):
        if (fn.find('.DS')==-1):
            #print fn
            fin = open(os.path.join(topdir, fn), 'rb')
            doc = str.decode(fin.read(), "UTF-8", "ignore")
            resultset.append(doc)
            tempid = doc[doc.find('ID')+3:doc.find('\n')]
            nameid.append(tempid)
            i = i+1
            fin.close()
    return resultset,nameid


# In[9]:

result,nameid = iter_docs('../RecommendationResult/IDFModel131')
#print len(result)
#print len(nameid)
#print result[130]
#print nameid[130]


# In[10]:

def findId(targetname,othername,docname):
    targetname = targetname.strip()
    targetname = targetname.replace(' ','')
    for i in range(len(docname)):
        temp = docname[i]
        temp = temp.strip()
        if(targetname==temp):
            return i
    print 'donfind'
    print targetname
    return 0


# In[11]:

def iter_docs_result(topdir):
    resultset = []
    nameid = []
    i = 0
    for fn in os.listdir(topdir):
        if (fn.find('.DS')==-1):
            #print fn
            fin = open(os.path.join(topdir, fn), 'rb')
            doc = str.decode(fin.read(), "UTF-8", "ignore")
            resultset.append(doc)
            tempid = doc[doc.find('ID')+3:doc.find('\n')]
            nameid.append(tempid)
            i = i+1
            fin.close()
    return resultset


# In[12]:

def bfs(graph, start, end):
    #print start,end
    queue = []
    queue.append([start])
    num = 0
    while ((len(queue)!=0) & (num<=10000)):
        #print 'here'
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            #print path
            return len(path)
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
        num = num+1
    #print 'dontfound'
    return 5


# In[13]:

def evalution(result,nameid,authorMap,doctopic,othername,docname):
    total = 0
    for i in xrange(len(result)):
    #for i in xrange(1):
        temp = result[i][result[i].find('1.'):]
        line = temp.split('\n')
        targetid = int(nameid[i])
        targettopic = doctopic[targetid]
        averageLen = []
        for j in xrange(len(line)-1):
            name = line[j][line[j].find('.')+2:line[j].find(':')]
            origId = findId(name,othername,docname)
            path = bfs(authorMap,targetid,origId)
            averageLen.append(path)
            #print 'len',averageLen
        num = len(line)-1
        mediumLen = np.median(averageLen)
        total = total+mediumLen
        #print total
    return total/len(result)


# In[14]:

# result = iter_docs_result('../../RecommendationResult/IDFModel131')
# idfResult = evalution(result,nameid,authorMap,doctopic,othername,docname)
# print 'TF Result:',idfResult


# # In[ ]:

# result = iter_docs_result('../../RecommendationResult/TFModel131')
# idfResult1 = evalution(result,nameid,authorMap,doctopic,othername,docname)
# print 'IDF Result:',idfResult1


# In[17]:

result = iter_docs_result('../RecommendationResult/TFSessionModel131')
idfResult1 = evalution(result,nameid,authorMap,doctopic,othername,docname)
print 'TFSession Result:',idfResult1


# In[ ]:

result = iter_docs_result('../RecommendationResult/TFKeywordModel131')
idfResult1 = evalution(result,nameid,authorMap,doctopic,othername,docname)
print 'TFKeyword Result:',idfResult1


# In[ ]:

result = iter_docs_result('../RecommendationResult/TFSerMailModel131')
idfResult1 = evalution(result,nameid,authorMap,doctopic,othername,docname)
print 'TFMailist Result:',idfResult1



