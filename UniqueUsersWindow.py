import requests
from PyQt6 import QtWidgets

import designes_py.unique_users_design as design
from config import URL_API

from ya_api import getUniqueUsers


class UniqueUsersWindow(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self, os):
        super().__init__()
        self.setupUi(self)

        if os.text() == 'Windows 7 or 2008 Server':
            self.os = 'Windows'
        else:
            self.os = os.text()

        self.label_4.setText(self.os)
        
        self.pushButton_4.clicked.connect(self.visits)

        

    def visits(self):
        self.listWidget.clear()
        first_date = self.dateEdit.text()
        last_date = self.dateEdit_2.text()
        response = getUniqueUsers(self.os, first_date, last_date)

        for i in range(len(response['data'][0]['metrics'][0])):
            self.listWidget.addItem(f"{response['time_intervals'][i][0]} - {str(int(response['data'][0]['metrics'][0][i]))}")



