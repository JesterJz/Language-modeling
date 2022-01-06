# import string library function
import re
import pickle
import os
from pyvi import ViTokenizer
from tensorflow import keras

#read, clean text and build sequences

data = open('../data/news-corpus/sample/demo-title.txt', "r", encoding="utf-8")
sequences = []
INPUT_LENGTH = 3
for ln in data.readlines():
    ln = ln.lower()
    ln = re.sub("[\.\,\/\:\(\)\-\'\"\!\?]",'', ln)
    line = ViTokenizer.tokenize(ln)
    tokens = line.split()
    # print(tokens)
    for i in range(INPUT_LENGTH + 1, len(tokens)+1):
        seq = tokens[i-INPUT_LENGTH-1:i]
        line = ' '.join(seq)
        sequences.append(line)

#build dictionary from sequences
tokenizer = keras.preprocessing.text.Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\]^`{|}~ ') # Filter bỏ qua các ký tự
# Tương ứng từ sang các số
tokenizer.fit_on_texts(sequences)

#save tokenizer as dict
pickle.dump(tokenizer, open('../model/dict.pkl', 'wb'))

#convert sequences from text to digit is list integer
# Sau khi đã có bảng, chúng ta thực hiện chuyển từng từ thành số tương ứng ở trong tất cả các chuỗi
sequences_digit = tokenizer.texts_to_sequences(sequences)
print(sequences_digit[0][:-1])

pickle.dump(sequences_digit, open('../model/sequences_digit.pkl', 'wb'))

#vocab_size = len(tokenizer.word_index)+1
# len(a.keys())