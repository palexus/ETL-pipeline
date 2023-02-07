import pymongo
from time import sleep
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



analyzer = SentimentIntensityAnalyzer()

# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

sleep(10)  # seconds

# Select the database you want to use withing the MongoDB server
db = client.twitter

pg = create_engine('postgresql://docker_user:1234@postgresdb:5432/twitter', echo=True)

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500) UNIQUE,
    sentiment NUMERIC
);
''')


while True:
    docs = db.twitter.find()

    for doc in docs:
        print(doc)
        text = doc['text']
        score = analyzer.polarity_scores(text)["compound"]
        query = "INSERT INTO tweets VALUES (%s, %s) ON CONFLICT DO NOTHING;"
        pg.execute(query, (text, score))

    sleep(3)
