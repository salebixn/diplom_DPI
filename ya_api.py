import json

import requests
from requests_html import HTMLSession

from config import YA_TOKEN, YA_COUNTER_ID


session = HTMLSession()


metrika_headers = {
    'GET': '/management/v1/counters HTTP/1.1',
    'Host': 'api-metrika.yandex.net',
    'Authorization': f'OAuth {YA_TOKEN}',
    'Content-Type': 'application/x-yametrika+json'
}

metrika_url = f'https://api-metrika.yandex.net/stat/v1/data?ids={YA_COUNTER_ID}&metrics=ym:s:avgPageViews&dimensions=ym:s:operatingSystem'

def getOsList() -> list[str]:
    json_content_response = session.get(metrika_url, headers=metrika_headers).json()

    os_list = []

    for item in json_content_response['data']:
        for key in item.keys():
            if key == 'dimensions':
                os_list.append(f"{item['dimensions'][0]['name']}")

    return os_list


def getVisits(os: str, first_date, last_date) -> dict:
    first_date = {
        'year': first_date.split('.')[-1],
        'month': first_date.split('.')[1],
        'day': first_date.split('.')[0],
    }

    last_date = {
        'year': last_date.split('.')[-1],
        'month': last_date.split('.')[1],
        'day': last_date.split('.')[0],
    }
    
    url = f"""https://api-metrika.yandex.net/stat/v1/data/bytime?row_ids=%5B%5B%22{os}%22%5D%5D&date1={first_date['year']}
    -{first_date['month']}-{first_date['day']}&date2={last_date['year']}-{last_date['month']}-{last_date['day']}&group=day&
    dimensions=ym:s:operatingSystemName&ids={YA_COUNTER_ID}&accuracy=medium&metrics=ym:s:visits&lang=ru"""

    return requests.get(url).json()


def getViewsPages(os: str, first_date, last_date) -> dict:
    first_date = {
        'year': first_date.split('.')[-1],
        'month': first_date.split('.')[1],
        'day': first_date.split('.')[0],
    }

    last_date = {
        'year': last_date.split('.')[-1],
        'month': last_date.split('.')[1],
        'day': last_date.split('.')[0],
    }
    
    url = f"""https://api-metrika.yandex.net/stat/v1/data/bytime?row_ids=%5B%5B%22{os}%22%5D%5D&date1={first_date['year']}
    -{first_date['month']}-{first_date['day']}&date2={last_date['year']}-{last_date['month']}-{last_date['day']}&group=day&
    dimensions=ym:s:operatingSystemName&ids={YA_COUNTER_ID}&accuracy=medium&metrics=ym:s:pageviews&lang=ru"""

    return requests.get(url).json()


def getUniqueUsers(os: str, first_date, last_date) -> dict:
    first_date = {
        'year': first_date.split('.')[-1],
        'month': first_date.split('.')[1],
        'day': first_date.split('.')[0],
    }

    last_date = {
        'year': last_date.split('.')[-1],
        'month': last_date.split('.')[1],
        'day': last_date.split('.')[0],
    }
    
    url = f"""https://api-metrika.yandex.net/stat/v1/data/bytime?row_ids=%5B%5B%22{os}%22%5D%5D&date1={first_date['year']}
    -{first_date['month']}-{first_date['day']}&date2={last_date['year']}-{last_date['month']}-{last_date['day']}&group=day&
    dimensions=ym:s:operatingSystemName&ids={YA_COUNTER_ID}&accuracy=medium&metrics=ym:s:users&lang=ru"""

    return requests.get(url).json()