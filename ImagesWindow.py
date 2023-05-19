import os

import requests
from PyQt6 import QtWidgets, QtGui

import designes_py.images_design as design
from config import URL_API


class ImagesWindow(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self, project_id):
        super().__init__()
        self.setupUi(self)

        self.project_id = project_id.text().replace(' ', '').split('-')[0]
        images = requests.get(f'{URL_API}/images/{self.project_id}').json()
        
        for image in images:
            response = requests.get(image['image'])

            if response.status_code != 404:
                with open(f"./projects_images_cache/{image['image'].split('/')[-1]}", 'wb') as file:
                    file.write(response.content)

                pixmap = QtGui.QPixmap(f"./projects_images_cache/{image['image'].split('/')[-1]}").scaled(200, 200)
                lbl = QtWidgets.QLabel(self)
                lbl.setPixmap(pixmap)
                self.horizontalLayout.addWidget(lbl)
                
            else:
                self.label.setText('Нет изображений')


        self.pushButton_7.clicked.connect(self.selectMultiFiles)


    def closeEvent(self, event):
        dir = './projects_images_cache'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

    def selectMultiFiles(self):
        filter = "PNG (*.png);;JPG (*.JPG)"
        file_window = QtWidgets.QFileDialog()
        files = file_window.getOpenFileNames(self, "Open files", "/home/qt/projects_images_cache", filter)
        print(files)
        if files:
            for filename in files[0]:
                print(f'filename:{filename}')
                self.uploadFile(filename)

    def uploadFile(self, filepath):
        filename = filepath
        # with open(filepath, 'rb') as f:
        #     file_content = QByteArray(f.read())

        with open(f'{filename}', 'rb') as f:
            response = requests.post(f'{URL_API}/upload-images/', data={'project_id': self.project_id}, files={'file': f})

        # url = f'{URL_API}/upload-files'
        # data = {'file': (file_name, file_content)}
        # response = requests.post(url, files=data)
