import transformers
from flask import Flask, request
from transformers import AutoTokenizer
from transformers import pipeline

# import torch
import numpy as np

model = transformers.TFAutoModelForSequenceClassification.from_pretrained("models/diagnosis_model")
checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint, use_fast=True)
model_input = pipeline(task="text-classification", model= model, tokenizer=tokenizer)
labels = ['allergy', 'arthritis', 'bronchial asthma', 'cervical spondylosis', 'chicken pox', 'common cold', 'dengue', 'diabetes', 'drug reaction', 'fungal infection', 'gastroesophageal reflux disease', 'hypertension', 'impetigo', 'jaundice', 'malaria', 'migraine', 'peptic ulcer disease', 'pneumonia', 'psoriasis', 'typhoid', 'urinary tract infection', 'varicose veins']

app = Flask(__name__)

@app.route('/models/diagnosis_model/v1', methods=['GET'])
def model_info():
   return {
      "version": "v1",
      "name": "diagnosis_model",
      "description": "Classify text containing symptoms (one of 22 diagnoses)",
      "pretrained_model": "distilbert-base-uncased",
      "diagnoses": labels
   }

@app.route('/models/diagnosis_model/v1', methods=['POST'])
def classify_clothes_image():
   text = request.json.get('text')
   if not text:
      return {"error": "The 'text' field is required"}, 404
   result = model_input(text)[0]
   return postprocess(result)

def postprocess(a):
   """
   Converts output into an readable output.
   """
   index = int(a["label"][6:])
   return {"diagnosis":labels[index], "score": a["score"]}

# start the development server
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')