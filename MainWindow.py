import requests
from PyQt6 import QtWidgets

import designes_py.main_design as design
from config import URL_API
from AddProjectWindow import AddProjectWindow
from UpdateProjectWindow import UpdateProjectWindow
from ImagesWindow import ImagesWindow
from DeleteProjectWindow import DeleteProjectWindow
from VisitsWindow import VisitsWindow
from ViewsPagesWindow import ViewsPagesWindow
from UniqueUsersWindow import UniqueUsersWindow
from SmsSendWindow import SmsSendWindow

from ya_api import getOsList


class MainWindow(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Проекты
        self.updateProjectsList()

        # Используемые ОС
        os_list = getOsList()
        for os in os_list:
            self.listWidget_2.addItem(f"{os}")

        # Заявки
        self.updateApplications()


        self.pushButton_3.clicked.connect(self.openUpdateProject)
        self.pushButton_4.clicked.connect(self.openAddProject)
        self.pushButton_5.clicked.connect(self.updateProjectsList)
        self.pushButton_6.clicked.connect(self.openImages)
        self.pushButton_7.clicked.connect(self.deleteProject)
        self.pushButton_8.clicked.connect(self.openVisits)
        self.pushButton_9.clicked.connect(self.openViewsPages)
        self.pushButton_10.clicked.connect(self.openUniqueUsers)
        self.pushButton_11.clicked.connect(self.updateApplications)
        self.pushButton_12.clicked.connect(self.sendSms)


    def openAddProject(self):
        self.window = AddProjectWindow()
        self.window.show()

    def openUpdateProject(self):
        try:
            self.window = UpdateProjectWindow(self.listWidget.currentItem())
            self.window.show()
        except Exception:
            pass

    def updateProjectsList(self):
        self.projects = requests.get(f'{URL_API}/projects/').json()
        self.listWidget.clear()
        for project in self.projects:
            self.listWidget.addItem(f"{project['id']} - {project['name']}")

    def openImages(self):
        try:
            self.window = ImagesWindow(self.listWidget.currentItem())
            self.window.show()
        except Exception:
            pass

    def deleteProject(self):
        try:
            self.window = DeleteProjectWindow(self.listWidget.currentItem())
            self.window.show()
        except Exception:
            pass

    def openVisits(self):
        try:
            self.window = VisitsWindow(self.listWidget_2.currentItem())
            self.window.show()
        except Exception:
            pass

    def openViewsPages(self):
        try:
            self.window = ViewsPagesWindow(self.listWidget_2.currentItem())
            self.window.show()
        except Exception:
            pass

    def openUniqueUsers(self):
        try:
            self.window = UniqueUsersWindow(self.listWidget_2.currentItem())
            self.window.show()
        except Exception:
            pass

    def updateApplications(self):
        self.applications = requests.get(f'{URL_API}/applications/').json()
        self.listWidget_3.clear()

        for application in self.applications:
            application_dict = {
                'year': application['date'].split('T')[0].split('-')[0],
                'month': application['date'].split('T')[0].split('-')[1],
                'day': application['date'].split('T')[0].split('-')[-1],
                'hours': str(int(application['date'].split('T')[1].split('.')[0].split(':')[0]) + 3),
                'minutes': application['date'].split('T')[1].split('.')[0].split(':')[1]
            }
            self.listWidget_3.addItem(f"{application_dict['day']}:{application_dict['month']}:{application_dict['year']} {application_dict['hours']}:{application_dict['minutes']} - {application['phone']}")

    def sendSms(self):
        try:
            self.window = SmsSendWindow(self.listWidget_3.currentItem())
            self.window.show()
        except Exception:
            pass