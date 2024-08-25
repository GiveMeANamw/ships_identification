import sys

from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic.properties import QtWidgets

from ui import Ui_MainWindow
from Camera_main import *


class login_window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(login_window, self).__init__()
        self.setupUi(self)  # 创建窗体对象
        self.init()
        self.admin = "123456"
        self.Password = "123456"

    def init(self):
        self.pushButton.clicked.connect(self.login_button)  # 连接槽

    def login_button(self):
        if self.lineEdit.text() == "":
            QMessageBox.warning(self, '警告', '账号不能为空，请输入！')
            return None

        if self.lineEdit_2.text() == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请输入！')
            return None

        if (self.lineEdit.text() == self.admin) and self.lineEdit_2.text() == self.Password:
            # 1打开新窗口
            Ui_Main.show()
            # 2关闭本窗口
            self.close()
        else:
            QMessageBox.critical(self, '错误', '账号或密码错误！')
            self.lineEdit.clear()
            return None


if __name__ == '__main__':
    from PyQt5 import QtCore, QtWidgets

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应分辨率
    app = QtWidgets.QApplication(sys.argv)
    window = login_window()
    Ui_Main = Open_Camera()  # 生成主窗口的实例
    window.show()
    sys.exit(app.exec_())