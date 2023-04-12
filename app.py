import textdistance
import re
import nltk
import pymorphy2
from nltk.corpus import stopwords
nltk.download('stopwords')
morph = pymorphy2.MorphAnalyzer()
nltk.download('punkt')

import gensim.downloader as api

from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route("/", methods=['POST', 'GET'])
def predict():
    word_1 = request.form["word"]
    word_2 = request.form["word_2"]
    model = api.load("glove-wiki-gigaword-50")
    model.similarity(word_1, word_2)
    tokenized_1 = []
    tok_sen = ''
    txt = re.findall(r'[a-z]+', word_1.lower())
    for j in txt:
      if j not in stopwords.words('english'):
        w = morph.parse(j)[0].normal_form
        if tok_sen == '':
          tok_sen += w
        else:
          tok_sen += (' ' + w)
    tokenized_1.append(tok_sen)

    tokenized_2 = []
    tok_sen = ''
    txt = re.findall(r'[a-z]+', word_2.lower())
    for j in txt:
      if j not in stopwords.words('english'):
        w = morph.parse(j)[0].normal_form
        if tok_sen == '':
          tok_sen += w
        else:
          tok_sen += (' ' + w)
    tokenized_2.append(tok_sen)
    data = textdistance.cosine(str(tokenized_1), str(tokenized_2))
    return render_template('index.html', data=f'Слова {word_1} и {word_2} похожи на: {data}', word_1 = request.form["word"], word_2 = request.form["word_2"])
    

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="5000")

