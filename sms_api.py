import datetime

import requests


def sendSmsMessage(number: str, text: str) -> None:
    login = 'prohousenn'
    password  = '123Gfhjkm567'
    url = f'https://smsc.ru/sys/send.php?login={login}&psw={password}&phones={number}&mes={text}'

    try:
        requests.get(url)
        with open('logs.log', 'a') as file:
            file.write(f'{datetime.datetime.now()} - SMS send success')
    except Exception as e:
        with open('logs.log', 'a') as file:
            file.write(f'{datetime.datetime.now()} - SMS: {e}')