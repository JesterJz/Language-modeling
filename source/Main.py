from flask import Flask, render_template, request
import re
import pickle
from pyvi import ViTokenizer
import pickle
import numpy as np

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

app = Flask(__name__)
global tokenizer, model

def gen_doc(doc, tokenizer):
    doc = doc.lower()
    ln = re.sub("[\.\,\/\:\(\)\-\'\"\!\?]",'', doc)
    line = ViTokenizer.tokenize(ln)
    tokens = line.split()
    tokens = tokens[-3:]
    seq_digit = tokenizer.texts_to_sequences([tokens])
    sequences = pad_sequences(seq_digit, maxlen=3)
    sequences = np.reshape(sequences, (1,3))
    sequences = np.array(sequences)
    return sequences

def generate_text(text_input, n_words, tokenizer, model):
    tokens = gen_doc(text_input, tokenizer)
    next_word = []
    for _ in range(n_words):
        next_digit = np.argmax(model.predict([tokens]))
        next_word.append(next_digit)
        tokens = np.append(tokens, next_digit)
        tokens = np.delete(tokens, 0)
        tokens = np.reshape(tokens, (1,3))
      
    tokens = np.reshape(tokens, (3))
    out_word = []
    for token in next_word:
        for word, index in tokenizer.word_index.items():
            if index == token:
                out_word.append(word)
                break
    return out_word

@app.route("/" , methods=['GET', 'POST']) 
def index():
    # global output
    if request.method == "POST":
        query = request.values['search'] or ''
        number = request.values['number']
        output = generate_text(query, int(number), tokenizer, model)
        return render_template('index.html', pages = output)
    return render_template('index.html')

if __name__ == "__main__":
    # Load the model and tokenizer
    model = load_model('../model/next_word.h5')
    print("Model: OK")
    with open('../model/tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
    print("Tokenizer: OK")
    print(len(tokenizer.word_index))
    app.run(port=8888, debug=True)