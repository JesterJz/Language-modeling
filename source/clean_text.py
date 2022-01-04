# import string library function
from pyvi import ViTokenizer
import re

#read, clean and build dict
data = open('../data/news-corpus/sample/demo-title.txt', "r", encoding="utf-8")
dictionary = []
for ln in data.readlines():
    ln = ln.lower()
    word = ViTokenizer.tokenize(ln)
    for word in word.split():
        word = re.sub("[\.\,\/\:\(\)\-\'\"\!\?]",'', word)
        if(len(word)!=0) and (word not in dictionary):
            dictionary.append(str(word))

#write bin file format utf8 dict

file = open('../model/dict.bin', "wb")
for dic in dictionary:
    dic = dic + '\n'
    file.write(dic.encode('utf-8'))
file.close()

#read bin file format utf8 dict
file = open('dict.bin','r', encoding='utf-8')
for line in file.readlines():
    print(line)