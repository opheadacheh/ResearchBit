import os
from xml.dom.minidom import parse
import time
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sets import Set

id2index = {}
index2id = {}


def GetStopWords(path):
    with open(path) as text_file:
        f = text_file.read()
    return f.split(' ')


def RewriteAuthorMap(path):
    with open(path, 'r') as text_file:
        text = text_file.read()
    with open(path, 'w+') as text_file:
        text_file.write(text.replace('None', '').replace(' ', '').replace('[', '').replace(']', '').replace('\'', '').replace(',\n', '\n'))
    return


def GetProfiles(dir_path):
    profiles = []
    name = []
    n = 0
    global id2index
    for fn in os.listdir(dir_path):
        fin = open(os.path.join(dir_path, fn), 'rb')
        xml = parse(fin)
        profile = ''
        for node in xml.getElementsByTagName('Text'):
            str = node.toxml()
            profile += str[str.find('>') + 1: str.rfind('<')]
        for node in xml.getElementsByTagName('Abstract'):
            str = node.toxml()
            profile += str[str.find('>') + 1: str.rfind('<')]
        profiles.append(profile)
        name.append(fn[8: -4].title())
        user_id = int(fn[3: 8])
        id2index[user_id] = n
        index2id[n] = user_id
        fin.close()
        n += 1
    return profiles, name


def GetAuthorMap(path):
    author_map = {}
    with open(path) as text_file:
        text = text_file.read()
    author_sets = text.split('\n')
    for authors in author_sets:
        authors = authors.split(',')
        if len(authors) > 1:
            for author in authors:
                author_id = author[author.find('ATT') + 3:]
                author_id = int(author_id)
                if author_id not in author_map.keys():
                    author_map[author_id] = Set()
                for other_author in authors:
                    other_author_id = other_author[other_author.find('ATT') + 3:]
                    other_author_id = int(other_author_id)
                    if (other_author_id not in author_map[author_id]) and (other_author_id != author_id):
                        author_map[author_id].add(other_author_id)
    return author_map


def Output(profile_matrix, name, authorMap, listsize, output_dir_path):
    n = profile_matrix.shape[0]
    for i in range(n):
        result = cosine_similarity(profile_matrix[i], profile_matrix)
        result = result[0]
        index = [j[0] for j in sorted(enumerate(result), key=lambda x: x[1], reverse=True)]
        fout = open(os.path.join(output_dir_path, name[i] + '.txt'), 'w+')
        if result[index[0]] > 0.9:
            num_recommended = 0
            j = 0
            while num_recommended < listsize:
                if index[j] == i:
                    j += 1
                    continue
                if (index2id[i] not in authorMap.keys()) or (index2id[index[j]] not in authorMap[index2id[i]]):
                    fout.write(name[index[j]] + ': ' + str(result[index[j]]) + '\n')
                    num_recommended += 1
                j += 1

# RewriteAuthorMap('../New_Data/authormap.txt')

start = time.time()
stop_words = GetStopWords('../New_Data/stopwords.txt')
print('Building stop words takes %f seconds'% (time.time() - start))

start = time.time()
profiles, name = GetProfiles('../New_Data/Profiles')
print('Building profiles takes %f seconds'% (time.time() - start))

start = time.time()
tfidf_vectorizer = TfidfVectorizer(norm=None, stop_words=stop_words, use_idf=False)
profile_feature_matrix = tfidf_vectorizer.fit_transform(profiles)
print('Building feature matrix takes %f seconds'% (time.time() - start))

start = time.time()
author_map = GetAuthorMap('../New_Data/authormap.txt')
print('Building author map takes %f seconds'% (time.time() - start))

start = time.time()
Output(profile_feature_matrix, name, author_map, 10, '../New_Data/Results/Recommendations')
print('Outputing takes %f seconds'% (time.time() - start))