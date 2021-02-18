import pickle
import os
from google.cloud import storage
import ast
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

# def access_secret_version(secret_id):
#     project_id = os.environ["GCP_PROJECT"]
#     version_id = 1

#     client = secretmanager.SecretManagerServiceClient()
#     name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
#     response = client.access_secret_version(request={"name": name})
#     return response.payload.data.decode("UTF-8")

def text_sentiment(request):
    storage_client = storage.Client()
    bucket = storage_client.bucket('geeroar-ml-models')
    blob =  bucket.blob('sentiment_classifier.pickle')
    model_string = blob.download_as_string()

    model = pickle.load(ast.literal_eval(model_string))

    # json = request.get_json()
    # if not json:
    #     return 'You should send me JSON with a property "text"'
    # elif 'text' in json:
    #     return check_sentiment(json['text'])
    # else:

    return "Testing"
