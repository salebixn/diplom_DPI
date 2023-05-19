import requests
from PyQt6 import QtWidgets

import designes_py.update_project_design as design
from config import URL_API


class UpdateProjectWindow(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self, project_id):
        super().__init__()
        self.setupUi(self)

        materials = requests.get(f'{URL_API}/materials/').json()
        for material in materials:
            self.comboBox.addItem(f"{material['id']}-{material['name']}")

        
        self.project_id = project_id.text().replace(' ', '').split('-')[0]
        project = requests.get(f'{URL_API}/projects/{self.project_id}').json()


        
        self.lineEdit_4.setText(project['name'])
        self.textEdit.setText(project['description']),
        self.lineEdit_5.setText(project['address']),
        self.doubleSpinBox.setValue(float(project['floors']))
        self.spinBox.setValue(int(project['sleeping_places']))
        self.spinBox_2.setValue(int(project['parking_place']))
        self.spinBox_3.setValue(int(project['bathrooms']))
        self.spinBox_4.setValue(int(project['total_area']))
        self.spinBox_5.setValue(int(project['built_up_area']))
        self.spinBox_6.setValue(int(project['living_space']))
        self.spinBox_7.setValue(int(project['price']))
        self.checkBox.setChecked(True) if project['price_on_text'] == 'true' else self.checkBox.setChecked(False)
        self.comboBox.setCurrentIndex(project['material']-1)
        self.checkBox_2.setChecked(True) if project['premium_or_not'] == 'true' else self.checkBox_2.setChecked(False)
    


        self.pushButton_5.clicked.connect(self.update_project)

    def update_project(self):
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
        
        response = requests.put(f'{URL_API}/projects/{self.project_id}/', data=d)
        self.close()