import pickle
import os
from google.cloud import secretmanager
from google.cloud import storage

import nltk
# nltk.data.path = ['.nltk']

# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from string import punctuation


# exclusions = set(stopwords.words('english') + punctuation)

# def extract_features(words):
#     return [w.lower() for w in words if w.lower() not in exclusions]

# def to_feature_map(words):
#     feature_map = {}
#     for w in words:
#         feature_map[w] = True
#     return feature_map

# def check_sentiment(text):
#     words = word_tokenize(text)
#     feature_map = to_feature_map(extract_features(words))
#     return model.classify(feature_map)

def access_secret_version(secret_id):
    project_id = os.environ["GCP_PROJECT"]
    version_id = 1

    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def text_sentiment(request):
    secret_id = "GC_FUNCTION_SA"
    client = storage.Client()
    bucket = client.get_bucket('geeroar-ml-models')
    blob = storage.Blob('sentiment_classifier.pickle', bucket)

    with open('/tmp/sentiment_classifier.pickle') as file_obj:
        client.download_blob_to_file(blob, file_obj)

    with open('/tmp/sentiment_classifier.pickle') as file_obj:
        model = pickle.load(file_obj)


    # json = request.get_json()
    # if not json:
    #     return 'You should send me JSON with a property "text"'
    # elif 'text' in json:
    #     return check_sentiment(json['text'])
    # else:

    return "Testing"
