import uuid
import datetime

import requests
from PyQt6 import QtWidgets, QtCore

import designes_py.auth_design as design
from config import URL_API
from MainWindow import MainWindow


class AuthWindow(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
            
        self.setupUi(self) # Это нужно для инициализации нашего дизайна

        # Hide window header
        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        
        self.pushButton_2.clicked.connect(self.ok_click)

    def ok_click(self):
        username = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        
        url_referer = 'https://prohousenn.ru/admin/login/?next=/admin/'
        session = requests.Session()
        session.headers.update({'referer': url_referer})

        get_response = session.get(url_referer)
        csrf_token = get_response.cookies['csrftoken']
        post_response = session.post(url_referer, data={'csrfmiddlewaretoken': csrf_token, 
                                                        'username': username,
                                                        'password': password,
                                                        'next': '/admin/'})
        session.close()

        if post_response.url == url_referer:
            self.label_3.setText('Вы не правильно ввели данные')
        else:
            self.close()

            with open('user_uuid.txt', 'r') as file:
                user_uuid = file.read()
            auth = requests.get(f'{URL_API}/auth/?uuid={user_uuid}').json()
            if auth['auth'] == 'User does not exist':
                user_uuid = str(uuid.uuid4())
                with open('user_uuid.txt', 'w') as file:
                    file.write(user_uuid)
            
            requests.post(f'{URL_API}/auth/', data={'uuid': user_uuid})
            
            self.window = MainWindow()  # Создаём объект класса ExampleApp
            self.window.show()