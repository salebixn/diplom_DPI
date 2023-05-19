import os

import requests
from PyQt6 import QtWidgets

import designes_py.delete_project_design as design
from config import URL_API


class DeleteProjectWindow(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self, project_id):
        super().__init__()
        self.setupUi(self)

        self.project_id = project_id.text().replace(' ', '').split('-')[0]
        
        self.label_2.setText(project_id.text())


        self.pushButton_6.clicked.connect(self.cancelDelete)
        self.pushButton_7.clicked.connect(self.confirmDelete)



    def cancelDelete(self):
        self.close()

    def confirmDelete(self):
        requests.delete(f'{URL_API}/projects/{self.project_id}/')
        self.close()
        
