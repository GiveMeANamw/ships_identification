# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_openImage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openImage.setGeometry(QtCore.QRect(70, 50, 93, 28))
        self.pushButton_openImage.setObjectName("pushButton_openImage")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(200, 50, 321, 231))
        self.label_image.setFrameShape(QtWidgets.QFrame.Box)
        self.label_image.setObjectName("label_image")
        self.label_image.setScaledContents(True)  # 图片填充整个框
        self.pushButton_saveImage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_saveImage.setGeometry(QtCore.QRect(70, 100, 93, 28))
        self.pushButton_saveImage.setObjectName("pushButton_saveImage")
        self.pushButton_openFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openFile.setGeometry(QtCore.QRect(70, 390, 101, 31))
        self.pushButton_openFile.setObjectName("pushButton_openFile")
        self.label_txt = QtWidgets.QLabel(self.centralwidget)
        self.label_txt.setGeometry(QtCore.QRect(200, 450, 341, 201))
        self.label_txt.setFrameShape(QtWidgets.QFrame.Box)
        self.label_txt.setObjectName("label_txt")
        self.pushButton_saveFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_saveFile.setGeometry(QtCore.QRect(70, 450, 101, 28))
        self.pushButton_saveFile.setObjectName("pushButton_saveFile")
        self.label_filePath = QtWidgets.QLabel(self.centralwidget)
        self.label_filePath.setGeometry(QtCore.QRect(200, 380, 291, 61))
        self.label_filePath.setWordWrap(True)
        self.label_filePath.setObjectName("label_filePath")
        self.pushButton_openDirectory = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openDirectory.setGeometry(QtCore.QRect(70, 320, 93, 28))
        self.pushButton_openDirectory.setObjectName("pushButton_openDirectory")
        self.label_directoryPath = QtWidgets.QLabel(self.centralwidget)
        self.label_directoryPath.setGeometry(QtCore.QRect(200, 310, 291, 61))
        self.label_directoryPath.setWordWrap(True)
        self.label_directoryPath.setObjectName("label_directoryPath")
        self.label_imagePath = QtWidgets.QLabel(self.centralwidget)
        self.label_imagePath.setGeometry(QtCore.QRect(570, 60, 150,100))
        self.label_imagePath.setObjectName("label_imagePath")
        self.label_imagePath.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_openImage.clicked.connect(self.openImage)
        self.pushButton_saveImage.clicked.connect(self.saveImage)
        self.pushButton_openFile.clicked.connect(self.openTextFile)
        self.pushButton_saveFile.clicked.connect(self.saveTextFile)
        self.pushButton_openDirectory.clicked.connect(self.openDirectory)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_openImage.setText(_translate("MainWindow", "打开图像"))
        self.label_image.setText(_translate("MainWindow", "图片"))
        self.pushButton_saveImage.setText(_translate("MainWindow", "保存图像"))
        self.pushButton_openFile.setText(_translate("MainWindow", "打开文件"))
        self.label_txt.setText(_translate("MainWindow", "文本内容"))
        self.pushButton_saveFile.setText(_translate("MainWindow", "保存文件"))
        self.label_filePath.setText(_translate("MainWindow", "文件路径"))
        self.pushButton_openDirectory.setText(_translate("MainWindow", "打开文件夹"))
        self.label_directoryPath.setText(_translate("MainWindow", "文件夹路径"))
        self.label_imagePath.setText(_translate("MainWindow", "图片路径"))

    def openImage(self):  # 选择本地图片上传
        global imgName  # 这里为了方便别的地方引用图片路径，我们把它设置为全局变量
        imgName, imgType = QFileDialog.getOpenFileName(self.centralwidget, "打开图片", "", "*.jpg;;*.png;;All Files(*);;*.bmp")    # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
        print("imgName="+imgName)
        print("imgType="+imgType)
        path='D:\\ships_vision\\GUI\\runs\\detect\\exp2\\100001027.bmp'
        jpg = QtGui.QPixmap(path).scaled(self.label_image.width(), self.label_image.height())  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长宽

        self.label_image.setPixmap(jpg)  # 在label控件上显示选择的图片
        self.label_imagePath.setText(imgName)  # 显示所选图片的本地路径

    def saveImage(self):  # 保存图片到本地
        screen = QApplication.primaryScreen()
        pix = screen.grabWindow(self.label_image.winId())
        fd,type= QFileDialog.getSaveFileName(self.centralwidget, "保存图片", "", "*.jpg;;*.png;;All Files(*)")
        pix.save(fd)

    def openDirectory(self):  # 打开文件夹（目录）
        fd = QFileDialog.getExistingDirectory(self.centralwidget, "选择文件夹", "")
        self.label_directoryPath.setText(fd)

    def openTextFile(self):  # 选择文本文件上传
        fd,fp = QFileDialog.getOpenFileName(self.centralwidget, "选择文件", "", "*.txt;;All Files(*)")
        f=open(fd,'r')
        self.label_txt.setText(f.read())
        self.label_filePath.setText(fd)
        f.close()

    def saveTextFile(self):  # 保存文本文件
        fd,fp= QFileDialog.getSaveFileName(self.centralwidget, "保存文件", "", "*.txt;;All Files(*)")
        f=open(fd,'w')
        f.write(self.label_txt.text())
        f.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formObj = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(formObj)
    formObj.show()
    sys.exit(app.exec_())