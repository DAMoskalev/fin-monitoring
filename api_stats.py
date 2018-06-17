import conf
import requests
import datetime


def stats_time(hour_offset=0):
    return str(datetime.datetime.strptime(requests.get(conf.DATE_URL + conf.TOKEN).text, '"%Y-%m-%d %H:%M:%S"') +
               datetime.timedelta(hours=hour_offset))


def get_stats_api_url(start_period, end_period, *dates, direction, group='hour', api_url=conf.STATS_URL,
                      metrics='revenue', token=conf.TOKEN):
    str_date = ''
    for date in dates:
        str_date += str(date) + ','
    print(str_date)
    return str(
        api_url + '?day_from=' + str(start_period) + '&day_to=' + str(end_period) + '&date_time_hour=' + str_date +
        '&group=' + group + '&direction=' + direction + '&metrics=' + metrics + '&token=' + token)


def data_to_dict(data):
    pass


def stats_diff(data, offset):
    pass


if __name__ == '__main__':
    r = get_stats_api_url(stats_time(-26), stats_time(), stats_time(-24),
                          stats_time(), stats_time(-25), stats_time(-1),
                          direction='1')
    print(r)
    print(requests.get(r).text)
