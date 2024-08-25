import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QTextBrowser, QLabel, QDialog, QMainWindow
import time
from GUI.ImgDoesntExisit import Ui_img
from GUI.MainWindow import Ui_MainWindow
import detect as dt
import data_operations as db
import argparse
import time
from pathlib import Path

import cv2
import pymysql
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from GUI.regist import Regist_Ui
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized
import data_operations as db


class MyMainWindow(Ui_MainWindow):
    # def __init__(self, parent=None):
    #     super(MyMainWindow, self).__init__(parent)
    #     self.pushButton_4.clicked.connect(self.exit_application)
    def __init__(self, mainWindow):
        super().__init__()
        print("initUI")
        self.setupUi(mainWindow)
        self.retranslateUi(mainWindow)
        self.pushButton_4.clicked.connect(self.exit_application)
        self.pushButton.clicked.connect(self.openFolderDialog)
        self.pushButton_2.clicked.connect(self.comfirm)
        self.initUI()

    def initUI(self):
        pass

    def exit_application(self):
        print("点击退出按钮")
        QApplication.instance().quit()

    def test(self):
        print("这是选择图片按钮")

    file_path = "null"

    def openFolderDialog(self):
        print("processing")
        path1, types = QFileDialog.getOpenFileName(self.centralwidget, "选择图片", "", "图片文件 (*.png *.jpg *.bmp)")
        print(path1)
        self.file_path = path1
        print(types)

    def search_result_img(self):
        # 将这个类里面的file_path变为反斜杠形式
        # 将real_path变成适合进行sql查询的形式
        # 根据源文件路径查询结果路径
        print("searching")
        path = self.file_path
        real_path = path.replace("/", "\\")
        query_path = real_path.replace("\\", "\\\\")
        conn = db.connect_to_database()
        cur = db.create_cursor(conn)
        query = f"SELECT ResultImgFilePath FROM ships_vision WHERE ImgFileName = '{query_path}'"
        try:
            cur.execute(query)
            results = cur.fetchall()
            for row in results:
                print(row)  # 打印每一行数据
        except pymysql.Error as err:
            print(f"Error executing query: {err}")

        db.close_connection(cur, conn)
        return str(results[0][0])

    def search_result_txt(self):
        # 将这个类里面的file_path变为反斜杠形式
        # 将real_path变成适合进行sql查询的形式
        # 根据源文件路径查询结果路径
        print("searching")
        path = self.file_path
        real_path = path.replace("/", "\\")
        query_path = real_path.replace("\\", "\\\\")
        conn = db.connect_to_database()
        cur = db.create_cursor(conn)
        query = f"SELECT ResultTXTFilePath FROM ships_vision WHERE ImgFileName = '{query_path}'"
        try:
            cur.execute(query)
            results = cur.fetchall()
            for row in results:
                print(row)  # 打印每一行数据
        except pymysql.Error as err:
            print(f"Error executing query: {err}")

        db.close_connection(cur, conn)
        return str(results[0][0])
    def display_info(self,result,result_txt):
        # 将文本结果打印再browser2
        file_path = result_txt  # 替换成你的文件路径
        try:
            with open(file_path, "r") as file:
                content = file.read()  # 读取文本中全部内容
                self.textBrowser_2.setText(content)  # 在 QTextBrowser 中显示文本
        except FileNotFoundError:
            print(f"文件 {file_path} 不存在")

        bmp = QtGui.QPixmap(result).scaled(self.label_4.width(),
                                        self.label_4.height())  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长宽
        # 图片结果打印在lable4
        self.label_4.setPixmap(bmp)

    def comfirm(self):
        print("file path is", self.file_path)
        if self.file_path == "null" or self.file_path == "":
            print("图像不存在")
            img = QDialog()
            ui_img = Ui_img()
            ui_img.setupUi(img)
            img.show()
            img.exec_()
        else:
            real_path = self.file_path.replace("/", "\\")
            # res是根据源文件路径查询得到的结果

            if dt.already_exist(real_path):
                self.textBrowser.setText("图片已被查询过")
                res = self.search_result_img()
                res_txt=self.search_result_txt()
                self.display_info(res,res_txt)
            else:
                print("图像正在识别中")
                # textBrowser是结果显示的文本框
                self.textBrowser.setText("Scanning")
                opt = dt.parse_args(real_path)
                check_requirements(exclude=('pycocotools', 'thop'))

                with torch.no_grad():
                    if opt.update:  # update all models (to fix SourceChangeWarning)
                        for opt.weights in ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt', 'yolov5x.pt']:
                            dt.detect(opt)
                            strip_optimizer(opt.weights)
                    else:
                        dt.detect(opt)
                res = self.search_result_img()
                res_txt=self.search_result_txt()
                print("res is "+res)
                self.display_info(res,res_txt)

            # 如果文件路径已经在数据库中，不需要调用detect
            # 如果文件路径不在数据库中，调用detect进行识别
            # 将识别到的图片结果加到图片框中
            # 将文本结果插入到文本框中




if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    form = MyMainWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
