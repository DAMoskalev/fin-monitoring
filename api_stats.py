import conf
import requests
import datetime
import json


# Получение последнего часа, за который собрана статистика
def stats_time_api(hour_offset=0):
    return str(datetime.datetime.strptime(requests.get(conf.DATE_URL + conf.TOKEN).text, '"%Y-%m-%d %H:%M:%S"') +
               datetime.timedelta(hours=hour_offset))


# Для использования при известном последнем часе. Уменьшает количество
# запросов к api
def stats_time(date=stats_time_api(), hour_offset=0):
    return str(datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S') +
               datetime.timedelta(hours=hour_offset))


# Получение url запроса к статистике. Отдает json.
def get_stats_api_url(start_period, end_period, *dates, direction, group='hour', api_url=conf.STATS_URL,
                      metrics='revenue', token=conf.TOKEN):
    str_date = ''
    for date in dates:
        str_date += str(date) + ','
    return str(
        api_url + '?day_from=' + str(start_period) + '&day_to=' + str(end_period) + '&date_time_hour=' + str_date +
        '&group=' + group + '&direction=' + direction + '&metrics=' + metrics + '&token=' + token)


# Конвертация json из stats в словарь
def data_to_dict(data):
    return json.loads(data)


# Сравнение данных статистики: сравниваем сегодня и вчера, дефолтно за последний час.
# Возврат процентов и суммы. offset в часах
def stats_diff(data,  date=stats_time(), offset=-24):
    def get_revenue(value):
        return value.get('revenue')
    print(date)
    print(get_revenue(data.get(date)))
    print(stats_time(date, offset))
    print(get_revenue(data.get(stats_time(date, offset))))


if __name__ == '__main__':
    n = stats_time()
    r = get_stats_api_url(stats_time(n, -26), stats_time(n), stats_time(n, -24),
                          stats_time(n), stats_time(n, -25), stats_time(n, -1),
                          direction='1')

    js = '{"2018-06-16 05:00:00":{"hour":"2018-06-16 05:00:00","revenue":"6934.24401707493"},"2018-06-16 06:00:00":{"hour":"2018-06-16 06:00:00","revenue":"6683.29926335811"},"2018-06-17 05:00:00":{"hour":"2018-06-17 05:00:00","revenue":"6530.28384547917"},"2018-06-17 06:00:00":{"hour":"2018-06-17 06:00:00","revenue":"6741.3182059621"}}'

    stats_diff(data_to_dict(requests.get(r).text))
