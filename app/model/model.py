import pickle 
import re
import numpy as np

with open("/app/model/trained_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]

def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"\[|\]", " ", text) 
    text = text.lower()
    pred = model.predict([text])
    pred_str = str(pred[0])
    pred_index = classes.index(pred_str)
    return classes[pred_index]

