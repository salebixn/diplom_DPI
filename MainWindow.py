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

from ya_api import getOsList


class MainWindow(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.projects = requests.get(f'{URL_API}/projects/').json()
        for project in self.projects:
            self.listWidget.addItem(f"{project['id']} - {project['name']}")

        os_list = getOsList()
        for os in os_list:
            self.listWidget_2.addItem(f"{os}")

        self.pushButton_3.clicked.connect(self.openUpdateProject)
        self.pushButton_4.clicked.connect(self.openAddProject)
        self.pushButton_5.clicked.connect(self.updateProjectsList)
        self.pushButton_6.clicked.connect(self.openImages)
        self.pushButton_7.clicked.connect(self.deleteProject)
        self.pushButton_8.clicked.connect(self.openVisits)
        self.pushButton_9.clicked.connect(self.openViewsPages)
        self.pushButton_10.clicked.connect(self.openUniqueUsers)

    def openAddProject(self):
        self.window = AddProjectWindow()
        self.window.show()

    def openUpdateProject(self):
        self.window = UpdateProjectWindow(self.listWidget.currentItem())
        self.window.show()

    def updateProjectsList(self):
        self.projects = requests.get(f'{URL_API}/projects/').json()
        self.listWidget.clear()
        for project in self.projects:
            self.listWidget.addItem(f"{project['id']} - {project['name']}")

    def openImages(self):
        self.window = ImagesWindow(self.listWidget.currentItem())
        self.window.show()

    def deleteProject(self):
        self.window = DeleteProjectWindow(self.listWidget.currentItem())
        self.window.show()

    def openVisits(self):
        self.window = VisitsWindow(self.listWidget_2.currentItem())
        self.window.show()

    def openViewsPages(self):
        self.window = ViewsPagesWindow(self.listWidget_2.currentItem())
        self.window.show()

    def openUniqueUsers(self):
        self.window = UniqueUsersWindow(self.listWidget_2.currentItem())
        self.window.show()
