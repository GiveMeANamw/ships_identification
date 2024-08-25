import sys
import GUI.first
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from GUI.first import Ui_MainWindow
from PyQt5 import QtCore

from GUI.login import Ui_Form
from GUI.register import Ui_Register




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    form=QWidget()
    ui_login= Ui_Form()
    ui_login.setupUi(form)
    form.show()
    app.exec_()



