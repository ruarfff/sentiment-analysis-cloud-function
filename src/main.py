import pickle

import nltk
nltk.data.path = ['.nltk']

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

model_file = open('.models/sentiment_classifier.pickle', 'rb')
model = pickle.load(model_file)
model_file.close()

exclusions = set(stopwords.words('english') + punctuation)

def extract_features(words):
    return [w.lower() for w in words if w.lower() not in exclusions]

def to_feature_map(words):
    feature_map = {}
    for w in words:
        feature_map[w] = True
    return feature_map

def check_sentiment(text):
    words = word_tokenize(text)
    feature_map = to_feature_map(extract_features(words))
    return model.classify(feature_map)

def text_sentiment(request):
    json = request.get_json()
    if not json:
        return 'You should send me JSON with a property "text"'
    elif 'text' in json:
        return check_sentiment(json['text'])
    else:
        return 'Error! No text found'
