
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


# In[2]:

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


# In[10]:

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


# In[11]:

result,nameid = iter_docs('../RecommendationResult/TFModel131')
result1,nameid1 = iter_docs('../RecommendationResult/TFKeywordModel131')
#print result[130]
#print nameid[130]
#print result1[130]
#print nameid1[130]


# In[12]:

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


# In[13]:

def evalution(result,result1,nameid,doctopic,othername,docname):
    total = []
    for i in xrange(len(result)):
    #for i in xrange(1):
        temp = result[i][result[i].find('1.'):]
        line = temp.split('\n')
        targetid = int(nameid[i])
        targettopic = doctopic[targetid]
        same = 0
        diff = 0
        list1 = []
        for j in xrange(len(line)-1):
            name = line[j][line[j].find('.')+2:line[j].find(':')]
            origId = findId(name,othername,docname)
            list1.append(origId)
        #print 'result'
        #print list1
        
        temp1 = result1[i][result1[i].find('1.'):]
        line1 = temp1.split('\n')
        targetid1 = int(nameid1[i])
        targettopic1 = doctopic[targetid1]
        list2 = []
        for j in xrange(len(line1)-1):
            name1 = line1[j][line1[j].find('.')+2:line1[j].find(':')]
            origId1 = findId(name1,othername,docname)
            list2.append(origId1)
        #print 'otherresult'
        #print list2
        
        for m in list1:
            for n in list2:
                if(m==n):
                    same = same+1
        total.append(same)
        
    #print total
    #print np.mean(total)
    return np.mean(total)/15


# In[14]:

result,nameid = iter_docs('../RecommendationResult/IDFModel131')
result1,nameid1 = iter_docs('../RecommendationResult/TFKeywordModel131')
idfResult = evalution(result,result1,nameid,doctopic,othername,docname)
print 'Keyword Result:',idfResult


# In[15]:

result,nameid = iter_docs('../RecommendationResult/IDFModel131')
result1,nameid1 = iter_docs('../RecommendationResult/TFSessionModel131')
idfResult = evalution(result,result1,nameid,doctopic,othername,docname)
print 'Session Result: ',idfResult


# In[16]:

result,nameid = iter_docs('../RecommendationResult/IDFModel131')
result1,nameid1 = iter_docs('../RecommendationResult/TFModel131')
idfResult = evalution(result,result1,nameid,doctopic,othername,docname)
print 'TF Result: ',idfResult


# In[ ]:


result,nameid = iter_docs('../../RecommendationResult/IDFModel131')
result1,nameid1 = iter_docs('../../RecommendationResult/TFSerMailModel131')
idfResult = evalution(result,result1,nameid,doctopic,othername,docname)
print 'Mailist Result: ',idfResult



