import re

import requests
from PyQt6 import QtWidgets
import matplotlib.pyplot as plt

import designes_py.visits_design as design
from config import URL_API

from ya_api import getVisits


class VisitsWindow(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self, os):
        super().__init__()
        self.setupUi(self)

        if os.text() == 'Windows 7 or 2008 Server':
            self.os = 'Windows'
        else:
            self.os = os.text()

        self.label_4.setText(self.os)
        
        self.pushButton_4.clicked.connect(self.visits)
        self.pushButton_5.clicked.connect(self.graphic)

        

    def visits(self):
        self.listWidget.clear()
        first_date = self.dateEdit.text()
        last_date = self.dateEdit_2.text()
        response = getVisits(self.os, first_date, last_date)

        

        for i in range(len(response['data'][0]['metrics'][0])):
            self.listWidget.addItem(f"{response['time_intervals'][i][0]} - {str(int(response['data'][0]['metrics'][0][i]))}")


    def graphic(self):
        self.listWidget.clear()
        first_date = self.dateEdit.text()
        last_date = self.dateEdit_2.text()
        response = getVisits(self.os, first_date, last_date)
        dates = []
        print(response['data'][0]['metrics'][0])
        for item in response['time_intervals']:
            dates.append(re.sub('202[0-9]-', '', item[0]))
        print(dates)
        plt.plot(dates, response['data'][0]['metrics'][0])
        plt.title('Визиты')
        plt.xlabel('Даты')
        plt.ylabel('Количество визитов')
        plt.xticks(fontsize=8, rotation=90)
        plt.show()
