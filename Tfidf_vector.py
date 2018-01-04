#encoding=utf-8
import os
import jieba
import jieba.posseg as pseg
import sys
import string
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import codecs
reload(sys)
sys.setdefaultencoding('utf8')


def getFilelist(argv):
    path ='E:/aa0011/test/process'
    filelist = []
    files = os.listdir(path)
    for f in files:
        if (f[0] == '.'):
            pass
        else:
            filelist.append(f)
    return filelist, path



def fenci(argv, path):


    aabb='E:/aa0011/test/fen'
    filename = argv
    f = open(path+'/'+filename,'r+')
    file_list = f.read()
    f.close()
    #stopwords = codecs.open("E:/aa0011/test/003.txt", "r", 'utf-8')
    linee=[line.strip().decode('utf-8') for line in open('E:/aa0011/test/004.txt').readlines()]
   # line = stopwords.readlines()
    #line= {}.fromkeys(['第一','第一回', '作者' ,'之后'])
    #stopwords = {}.fromkeys(['第一','第一回', '作者' ,'之后'])
    seg_list = jieba.cut(file_list, cut_all=True)


    result = []
    for seg in seg_list:
        seg = seg.encode('utf - 8')
        if seg in linee:
            seg = ''.join(seg.split())
            if (seg != '' and seg != "\n" and seg != "\n\n"):
             result.append(seg)

    #stopwords.close()
    f = open(aabb + "/" + filename, "w+")
    f.write(' '.join(result))
    f.close()



def Tfidf(filelist):
    path = 'E:/aa0011/test/fen/'
    corpus = []
    for ff in filelist:
        fname = path + ff
        f = open(fname, 'r+')
        content = f.read()
        f.close()
        corpus.append(content)
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    sFilePath = './tfidffile'
    if not os.path.exists(sFilePath):
        os.mkdir(sFilePath)


    for i in range(len(weight)):
         print ( u"--------Writing all the tf-idf in the", i, u" file into ", sFilePath + '/' + string.zfill(i, 5) + '.txt', "--------")
         f = open(sFilePath + '/' + string.zfill(i, 5) + '.txt', 'w+')
         for j in range(len(word)):
            f.write(word[j] + "    " + str(weight[i][j]) + "\n")
         f.close()

if __name__ == "__main__":
    (allfile, path) = getFilelist('w')
    for ff in allfile:
            print("Using jieba on " + ff)
            fenci(ff,path)

    Tfidf(allfile)