
# coding: utf-8

# In[1]:

from __future__ import division
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


# In[3]:

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


# In[16]:

result,nameid = iter_docs('../RecommendationResult/IDFModel131')
#print len(result)
#print len(nameid)
#print result[130]
#print nameid[130]


# In[17]:

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


# In[18]:

def evalution(result,nameid,doctopic,othername,docname):
    total = 0
    for i in xrange(len(result)):
    #for i in xrange(1):
        temp = result[i][result[i].find('1.'):]
        line = temp.split('\n')
        targetid = int(nameid[i])
        targettopic = doctopic[targetid]
        same = 0
        diff = 0
        for j in xrange(len(line)-1):
            name = line[j][line[j].find('.')+2:line[j].find(':')]
            origId = findId(name,othername,docname)
            if(targettopic==doctopic[origId]):
                same = same+1
            else:
                diff = diff+1
        num = len(line)-1
        total = total + (same/num - diff/num)
    return total/len(result)


# In[19]:

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


# In[20]:

result = iter_docs_result('../RecommendationResult/IDFModel131')
idfResult = evalution(result,nameid,doctopic,othername,docname)
print 'TF Result:',idfResult


# In[21]:

result = iter_docs_result('../RecommendationResult/TFModel131')
idfResult1 = evalution(result,nameid,doctopic,othername,docname)
print 'IDF Result:',idfResult1


# In[22]:

result = iter_docs_result('../RecommendationResult/TFSessionModel131')
idfResult1 = evalution(result,nameid,doctopic,othername,docname)
print 'IDFSession Result:',idfResult1


# In[15]:

result = iter_docs_result('../RecommendationResult/TFKeywordModel131')
idfResult1 = evalution(result,nameid,doctopic,othername,docname)
print 'IDFKeyword Result:',idfResult1


# In[ ]:
result = iter_docs_result('../../RecommendationResult/TFSerMailModel131')
idfResult1 = evalution(result,nameid,doctopic,othername,docname)
print 'IDFMailist Result:',idfResult1




# In[ ]:



