import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from csdn import Ui_MainWindow
class my_ComboBox(Ui_MainWindow):
    def __init__(self,mainWindow):
        super().__init__()
        self.setupUi(mainWindow)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.print)
    def print(self):
        print("hello")
        QApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    form = my_ComboBox(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
