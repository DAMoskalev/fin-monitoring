import api_slack
import conf

if __name__ == '__main__':
    print('start')
    api_slack.to_slack('тестовый текст', conf.SLACK_URL)

