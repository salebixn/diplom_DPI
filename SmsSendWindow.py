import datetime

import requests
from PyQt6 import QtWidgets

import designes_py.sms_design as design
from config import URL_API

from sms_api import sendSmsMessage


class SmsSendWindow(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self, application):
        super().__init__()
        self.setupUi(self)

        self.number = application.text().replace(' ', '').split('-')[1:]
        self.label_2.setText(''.join(self.number))

        self.pushButton_2.clicked.connect(self.cancelSms)
        self.pushButton_3.clicked.connect(self.submitSend)


    def submitSend(self):
        if self.textEdit.toPlainText() == '':
            self.label_3.setText('Введите сообщение')
        else:
            number = ''
            for digit in self.number:
                if digit not in ('(', ')'):
                    number += digit
            try:
                sendSmsMessage(number, self.textEdit.toPlainText())
                self.close()
            except Exception as e:
                with open('logs.log', 'a') as file:
                    file.write(f'{datetime.datetime.now()} - SMS: {e}')
                self.label_3.setText('Ошибка')


    def cancelSms(self):
        self.close()