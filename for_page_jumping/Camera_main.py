# here put the import lib
import sys
from PyQt5 import QtGui, QtWidgets
from Camera import Ui_mainWindow
import cv2
import time
from PyQt5.Qt import *


class Open_Camera(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(Open_Camera, self).__init__()
        self.setupUi(self)  # 创建窗体对象
        self.init()
        self.cap = cv2.VideoCapture()  # 初始化摄像头
        self.photo_flag = 0
        self.label.setScaledContents(True)  # 图片自适应
        self.label_2.setScaledContents(True)  # 图片自适应

    def init(self):
        # 定时器让其定时读取显示图片
        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self.show_image)
        # 打开摄像头
        self.pushButton.clicked.connect(self.open_camera)
        # 拍照
        self.pushButton_2.clicked.connect(self.taking_pictures)
        # 关闭摄像头
        self.pushButton_3.clicked.connect(self.close_camera)
        # 导入图片
        self.pushButton_4.clicked.connect(self.loadphoto)

    # 开启摄像头
    def open_camera(self):
        self.cap = cv2.VideoCapture(0)  # 摄像头
        self.camera_timer.start(40)  # 每40毫秒读取一次，即刷新率为25帧
        self.show_image()

    # 显示图片
    def show_image(self):
        flag, self.image = self.cap.read()  # 从视频流中读取图片
        width, height, _ = self.image.shape  # 行:宽，列:高
        ratio1 = width / self.label.width()  # (label 宽度)
        ratio2 = height / self.label.height()  # (label 高度)
        ratio = max(ratio1, ratio2)
        image_show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # opencv读的通道是BGR,要转成RGB
        image_show = cv2.flip(image_show, 1)  # 水平翻转，因为摄像头拍的是镜像的。
        # 把读取到的视频数据变成QImage形式(图片数据、高、宽、RGB颜色空间，三个通道各有2**8=256种颜色)
        self.showImage = QtGui.QImage(image_show.data, height, width, QImage.Format_RGB888)
        self.showImage.setDevicePixelRatio(ratio)  # 按照缩放比例自适应 label 显示
        self.label.setPixmap(QPixmap.fromImage(self.showImage))  # 往显示视频的Label里显示QImage
        # self.label.setScaledContents(True) # 图片自适应

    # 拍照
    def taking_pictures(self):
        if self.cap.isOpened():
            FName = fr"images/cap{time.strftime('%Y%m%d%H%M%S', time.localtime())}"
            print(FName)
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.showImage))
            # self.showImage.save(FName + ".jpg", "JPG", 100)
            self.showImage.save('./1.jpg')
        else:
            QMessageBox.critical(self, '错误', '摄像头未打开！')
            return None

    # 关闭摄像头
    def close_camera(self):
        self.camera_timer.stop()  # 停止读取
        self.cap.release()  # 释放摄像头
        self.label.clear()  # 清除label组件上的图片
        self.label_2.clear()  # 清除label组件上的图片
        self.label.setText("摄像头")
        # self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 摄像头

    # 导入图片
    def loadphoto(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', '../', 'Image files(*.jpg *.gif *.png*.bmp)')
        self.showImage = fname
        self.label_2.setPixmap(QPixmap(self.showImage).scaled(self.label_2.width(), self.label_2.height()))


if __name__ == '__main__':
    from PyQt5 import QtCore

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应分辨率
    app = QtWidgets.QApplication(sys.argv)
    ui = Open_Camera()
    ui.show()
    sys.exit(app.exec_())