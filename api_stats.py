import conf
import requests
import datetime


DATE_URL = 'http://1stats-api.rtty.in/api/v1/stats/last-hour?_format=&token=' + conf.TOKEN

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


# конвертер времени из stats для формирования url


def to_py_date(stats_date):
    return datetime.datetime.strptime(stats_date, '"%Y-%m-%d %H:%M:%S"')



    # узнать последний час
    today = to_py_date(requests.get(DATE_URL).text)
    yesterday = today - datetime.timedelta(days=1)
    hour_1 = datetime.timedelta(hours=1)
    hour_2 = datetime.timedelta(hours=2)
    hour_3 = datetime.timedelta(hours=3)
    url2 = 'http://1stats-api.rtty.in/api/v1/stats/?day_from=' + str(yesterday - hour_2) + \
           '&day_to=' + str(today) + \
           '&date_time_hour=' + str(today) + ',' + str(yesterday) + ',' \
           '&group=hour' \
           '&direction=1' \
           '&metrics=revenue' \
           '&token=' + conf.TOKEN
    print(url2)
    print(requests.get(url2).text)
    print(url1)

    # собрать разницу между последним и предпоследним часами
    # собрать разницу между 2 и 3 часа назад
    #print(requests.get(url).text)
 #   print(requests.get(url1).text)



