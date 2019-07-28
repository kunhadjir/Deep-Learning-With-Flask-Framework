from flask import Flask
from keras.models import load_model
from flask import request, json, Response, g, jsonify
from keras.preprocessing.text import one_hot
from keras.preprocessing import sequence
from keras import backend as K
from keras.datasets import imdb
from keras.layers import Embedding
import base64
import os
import numpy as np

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/predictservice', methods=['POST'])
def predictservice():
    if request.method == 'POST':
        K.clear_session()
        model = load_model('savemodel.h5')
        model.load_weights('saveweights.h5')

        array = []
        data = request.json
        teks = data['teks']

        array.append(teks)

        vocab_size = 5000
        encoded_teks = [one_hot(t, vocab_size) for t in array]

        max_words = 500
        encoded_teks = sequence.pad_sequences(encoded_teks, maxlen=max_words)

        hasil = ""
        predik = model.predict_classes(encoded_teks)

        if predik == 0:
            hasil = "positive"

        if predik == 1:
            hasil = "negative"

        return jsonify({"hasil": hasil})
        K.clear_session()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5150, debug=True)
