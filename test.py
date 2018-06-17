import conf
import json

TATS_URL = 'http://1stats-api.rtty.in/api/v1/stats/'

url1 = 'http://1stats-api.rtty.in/api/v1/stats/' \
       '?day_from=2018-06-15 08:00:00' \
       '&day_to=2018-06-16 10:00:00' \
       '&date_time_hour=' \
       '2018-06-16 10:00:00,2018-06-15 10:00:00,' \
       '2018-06-16 09:00:00,2018-06-16 08:00:00,' \
       '2018-06-15 09:00:00,2018-06-15 08:00:00,' \
       '&group=hour' \
       '&direction=1' \
       '&metrics=revenue' \
       '&token=' + conf.TOKEN

url = 'http://1stats-api.rtty.in/api/v1/stats/'


def js_parser(js):
    for i, j in js.items():
        print('{}: {}'.format(i, j))


if __name__ == '__main__':

    js = json.loads('{"2018-06-16 05:00:00":{"hour":"2018-06-16 05:00:00","revenue":"6934.24401707493"},'
                    '"2018-06-16 06:00:00":{"hour":"2018-06-16 06:00:00","revenue":"6683.29926335811"},'
                    '"2018-06-17 05:00:00":{"hour":"2018-06-17 05:00:00","revenue":"6530.28384547917"},'
                    '"2018-06-17 06:00:00":{"hour":"2018-06-17 06:00:00","revenue":"6741.3182059621"}}')

    js_parser(js)
