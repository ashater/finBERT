from flask import Flask
from flask_cors import CORS
import sys
import optparse
import time
from flask import request
import sys
from finbert.finbert import predict
#from pytorch_pretrained_bert.modeling import BertForSequenceClassification
from transformers import AutoModelForSequenceClassification
import nltk
import osf
import logging

nltk.download('punkt')
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)
start = int(round(time.time()))
#model = BertForSequenceClassification.from_pretrained('/src/models/classifier_model/finbert-sentiment', num_labels=3, cache_dir=None)
#model = BertForSequenceClassification.from_pretrained(r'C:\work\finbert\finBERT\models\sentiment\finbert-sentiment_20211104', num_labels=3, cache_dir=None)
#cl_path = r'C:\work\finbert\finBERT\models\sentiment\finbert-sentiment_20211104'
cl_path = '/src/models/classifier_model/finbert-sentiment'
model = AutoModelForSequenceClassification.from_pretrained(cl_path, cache_dir=None, num_labels=3)

@app.route("/",methods=['POST'])
def score():
    text=request.get_json()['text']
    results = predict(text, model)
    logger.info(results)
    
    return(results.to_json(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)
