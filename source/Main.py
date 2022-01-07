from flask import Flask, render_template, request
import re
import pickle
from pyvi import ViTokenizer
import pickle
import numpy as np

# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import load_model

app = Flask(__name__)

# # Load the model and tokenizer
# model = load_model('./model/next_word.h5')
# print("Model: OK")
# with open('./model/tokenizer.pkl', 'rb') as f:
#     tokenizer = pickle.load(f)
# print("Tokenizer: OK")
# len(tokenizer.word_index)


# def gen_doc(doc):
#   doc = doc.lower()
#   ln = re.sub("[\.\,\/\:\(\)\-\'\"\!\?]",'', doc)
#   line = ViTokenizer.tokenize(ln)
#   tokens = line.split()
#   tokens = tokens[-3:]
#   seq_digit = tokenizer.texts_to_sequences([tokens])
#   sequences = pad_sequences(seq_digit, maxlen=3)
#   sequences = np.reshape(sequences, (1,3))
#   sequences = np.array(sequences)
#   return sequences

# def generate_text(text_input, n_words):
#     tokens = gen_doc(text_input)

#     for _ in range(n_words):
#         next_digit = np.argmax(model.predict([tokens]))
#         tokens = np.append(tokens, next_digit)
#     out_word = []
#     for token in tokens:
#         for word, index in tokenizer.word_index.items():
#             if index == token:
#                 out_word.append(word)
#                 break
    # return ' '.join(out_word)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        query = request.values['search'] or ''
        print(query)
    #     # query = str(query.encode('utf-8'))
    #     # query = query.decode().encode("utf-8")
    #     query = query.lower()
    #     print ('query = ' + query)
    #     output = []
    #     try:
            

    # #             # print('hoài = ' + wordsimilar)
    #     except:
    #         output = 'Not found' + query
    return render_template('search.html')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8888, debug=True)