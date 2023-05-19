import requests
from PyQt6 import QtWidgets

import designes_py.add_project_design as design
from config import URL_API


class AddProjectWindow(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        materials = requests.get(f'{URL_API}/materials/').json()
        for material in materials:
            self.comboBox.addItem(f"{material['id']}-{material['name']}")

        self.pushButton_5.clicked.connect(self.add_project)

    def add_project(self):
        d={
            'name': self.lineEdit_4.text(),
            'uppered_name': self.lineEdit_4.text().upper(),
            'description': self.textEdit.toPlainText(),
            'address': self.lineEdit_5.text(),
            'floors': float(self.doubleSpinBox.text().replace(',', '.')),
            'sleeping_places': int(self.spinBox.text()),
            'parking_place': int(self.spinBox_2.text()),
            'bathrooms': int(self.spinBox_3.text()),
            'total_area': int(self.spinBox_4.text()),
            'built_up_area': int(self.spinBox_5.text()),
            'living_space': int(self.spinBox_6.text()),
            'price': int(self.spinBox_7.text()),
            'price_on_text': 'true' if self.checkBox.isChecked() is True else 'false',
            'material': int(self.comboBox.currentText().split('-')[0]),
            'premium_or_not': 'true' if self.checkBox_2.isChecked() is True else 'false'
        }
        
        response = requests.post(f'{URL_API}/projects/', data=d)
        self.close()