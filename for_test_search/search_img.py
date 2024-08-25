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

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized
import data_operations as db


def search_result_img(path):
    # 将这个类里面的file_path变为反斜杠形式
    # 将real_path变成适合进行sql查询的形式
    # 根据源文件路径查询结果路径
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

if __name__ == '__main__':
    path="D:/ships_vision/imgs/100001046.bmp"
    res=search_result_img(path)
    print("res is "+res)
