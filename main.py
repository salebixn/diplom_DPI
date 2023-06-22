import sys  # sys нужен для передачи argv в QApplication

import requests
from PyQt6 import QtWidgets

from config import URL_API
from AuthWindow import AuthWindow
from MainWindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    with open('user_uuid.txt', 'r') as file:
        user_uuid = file.read()
    auth = requests.get(f'{URL_API}/auth/?uuid={user_uuid}').json()
    if auth['auth'] == 1:
        window = MainWindow()
        window.show()
        app.exec()
    elif auth['auth'] == 0 or auth['auth'] == 'User does not exist':
        window = AuthWindow()
        window.show()
        app.exec()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()