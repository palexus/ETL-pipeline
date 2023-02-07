import requests
from time import sleep
from sqlalchemy import create_engine


webhook_url = "https://hooks.slack.com/services/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"

sleep(20)

pg = create_engine('postgresql://docker_user:1234@postgresdb:5432/twitter', echo=True)


def most_positive():
    result = pg.execute('''
            SELECT text, sentiment FROM tweets
	            WHERE sentiment = (SELECT MAX(sentiment) FROM tweets);
        ''')
    return result

def most_negative():
    result = pg.execute('''
            SELECT text, sentiment FROM tweets
	            WHERE sentiment = (SELECT MIN(sentiment) FROM tweets);
        ''')
    return result


while True:
    positive = most_positive()
    negative = most_negative()
    for pos in positive:
        print("positive: ", pos)
        data = {'text': "Most positive tweet: " + pos["text"]}
        requests.post(url=webhook_url, json = data)
    for neg in negative:
        print("negative: ", neg)
        data = {'text': "Most negative tweet: " + neg["text"]}
        requests.post(url=webhook_url, json = data)

    sleep(5)


#data = {'text': message}

#requests.post(url=webhook_url, json = data)