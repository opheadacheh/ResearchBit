from sklearn.feature_extraction.text import TfidfVectorizer

def readinStopWords():
    with open("../Data/stopwords.txt") as text_file:
        f = text_file.read()
    stops = f.split(" ")
    stop_words_list = stops

    for j in range(len(stop_words_list)):
        stop_words_list[j].decode("utf8")
    stopWords = [unicode(i,encoding='UTF-8') for i in stop_words_list]
    return stopWords

filein = open('../Data/Data/All_Profile_Data/ATT00000_davidjonesCompressed.txt')
str = filein.read()
StopWords = readinStopWords()
tfidf_vectorizer = TfidfVectorizer(norm=None, use_idf=False)
data = tfidf_vectorizer.fit_transform([str])
print data
print tfidf_vectorizer.get_feature_names()

#print data