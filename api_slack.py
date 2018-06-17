import requests


# Отправка простого текста в slack
def text_to_slack(message, url):
    text = {'text': message,
            'channel': 'py-fin-mon-test',
            'username': 'Fin mon',
            'icon_emoji': ':scream:'}
    requests.post(url, json=text)
    print(text)
