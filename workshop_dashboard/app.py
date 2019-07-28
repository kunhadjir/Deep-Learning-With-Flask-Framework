from flask import Flask
from flask import request, json, Response, Blueprint, g, jsonify,render_template
import os
import base64
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def input_image():
    return render_template('test.html')

@app.route('/upload',methods = ['POST'])
def upload():
    if request.method == 'POST':
        text = request.form['text']
        data = json.dumps({"teks":text})

        headers = {'Content-Type': 'application/json'}

        res = requests.post('http://localhost:5150/predictservice',headers=headers ,data= data)

        data = res.json()
        data = data['hasil']
        return render_template('hasil.html',data = data)

        #return res.text


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5500,debug=True)