import pandas as pd
import numpy as np
from fastapi.encoders import jsonable_encoder
import pickle
import spacy
import nltk
import text2emotion as te


# async def download_nltk():
#     try:
#         nltk.data.find('corpora/stopwords')
#         console.log('nltk stopwords exist')
#         return 1
#     except LookupError:
#         console.log('download nltk stopwords')
#         _ = await nltk.download('stopwords')
#         return 1


# if download_nltk():


# if download_ntlk():
#     print('nltk downloaded')
#     import text2emotion as te


# nlp = spacy.load("en_core_web_lg")


def vectorizer(text):
    with nlp.disable_pipes():
        vector = np.array(nlp(text).vector)
    return vector


def analysis(text):
    # prediction
    model = pickle.load(open('models/svc_model.sav', 'rb'))
    vectorized_text = pd.DataFrame(vectorizer(text).reshape(1, -1))
    prediction = model.predict_proba(vectorized_text).flatten()
    # emotions
    emotions = te.get_emotion(text)
    df = pd.DataFrame.from_dict(emotions, orient='index').sort_values(by=0, ascending=False).reset_index()
    df.columns = ['Emotion', 'Frequency']
    df = df[df['Frequency'] != 0]
    df['Frequency'] = df['Frequency'] * 100
    response = {
        'labels': df['Emotion'].tolist(),
        'data': df['Frequency'].tolist(),
        'positive': round(prediction[1] * 100, 2),
        'negative': round(prediction[0] * 100, 2),
    }
    return jsonable_encoder(response)


# get emotion data for piechart
# returns emotions for each positive/negative/all reviews
# all=0, positive=1, negative=2
def get_emotions(id):
    labels = []
    data = []
    if id == 0:
        df = pd.read_csv('fake_db/all_emotions.csv')
        labels = df['Emotion'].tolist()
        data = df['Frequency'].tolist()
    elif id == 1:
        df = pd.read_csv('fake_db/positive_emotions.csv')
        labels = df['Emotion'].tolist()
        data = df['Frequency'].tolist()
    elif id == 2:
        df = pd.read_csv('fake_db/negative_emotions.csv')
        labels = df['Emotion'].tolist()
        data = df['Frequency'].tolist()
    print(labels)
    print(data)
    response = {
        'labels': labels,
        'data': data
    }
    return jsonable_encoder(response)


# get most common nouns data for barchart
# returns common nouns for each positive/negative/all reviews
# all=0, positive=1, negative=2
def get_nouns(id):
    labels = []
    data = []
    if id == 0:
        df = pd.read_csv('fake_db/all_nouns.csv')
        labels = df.head(10)['nouns'].tolist()
        data = df.head(10)['count'].tolist()
    elif id == 1:
        df = pd.read_csv('fake_db/positive_nouns.csv')
        labels = df.head(10)['nouns'].tolist()
        data = df.head(10)['count'].tolist()
    elif id == 2:
        df = pd.read_csv('fake_db/negative_nouns.csv')
        labels = df.head(10)['nouns'].tolist()
        data = df.head(10)['count'].tolist()
    print(labels)
    print(data)
    response = {
        'labels': labels,
        'data': data
    }
    return jsonable_encoder(response)


# get most common phrases data for barchart
# returns common phrases for each positive/negative/all reviews
# all=0, positive=1, negative=2
def get_phrases(id):
    labels = []
    data = []
    if id == 0:
        df = pd.read_csv('fake_db/all_phrases.csv')
        labels = df.head(10)['phrases'].tolist()
        data = df.head(10)['count'].tolist()
    elif id == 1:
        df = pd.read_csv('fake_db/positive_phrases.csv')
        labels = df.head(10)['phrases'].tolist()
        data = df.head(10)['count'].tolist()
    elif id == 2:
        df = pd.read_csv('fake_db/negative_phrases.csv')
        labels = df.head(10)['phrases'].tolist()
        data = df.head(10)['count'].tolist()
    print(labels)
    print(data)
    response = {
        'labels': labels,
        'data': data
    }
    return jsonable_encoder(response)
