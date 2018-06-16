import requests


def to_slack(message, url):
    text = {'text': message,
            'channel': 'py-fin-mon-test',
            'username': 'Fin mon',
            'icon_emoji': ':scream:'}
    requests.post(url, json=text)
    print(text)
