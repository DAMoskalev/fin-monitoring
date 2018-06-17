import conf
import datetime

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


def arg_test(url, token, *dates):
    string_ = ''
    for i in dates:
        string_ += i + ','
    req = url + string_ + '&token=' + token
    print(req)
    pass


if __name__ == '__main__':
    date1 = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H-%M-%S')
    date2 = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(hours=1), '%Y-%m-%d %H-%M-%S')
    print(date1)
    print(date2)
    arg_test(url, conf.TOKEN, date1, date2)

    for i, j in conf.DIRECTIONS.items():
        print('{}: {}'.format(i, j))
