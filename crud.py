import pandas as pd
from fastapi.encoders import jsonable_encoder


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
