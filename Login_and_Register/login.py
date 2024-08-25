# -*- coding: utf-8 -*-
import pymysql
# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import Qt
from Login_and_Register.regist import *

import sys
import data_operations as db


global UserName
UserP = {}  #定义一个存储密码账号的元组
class Login_Ui(QWidget):
    def __init__(self):
        super(Login_Ui, self).__init__()
        self.re = Regist_Ui()  # 这边一定要加self
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(716, 371)
        Form.setMinimumSize(QtCore.QSize(716, 371))
        Form.setMaximumSize(QtCore.QSize(716, 371))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(380, 70, 331, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Login = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.Login.setFont(font)
        self.Login.setObjectName("Login")
        self.horizontalLayout.addWidget(self.Login)
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Logout = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.Logout.setFont(font)
        self.Logout.setObjectName("Logout")
        self.horizontalLayout.addWidget(self.Logout)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Regist = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.Regist.setFont(font)
        self.Regist.setObjectName("Regist")
        self.horizontalLayout.addWidget(self.Regist)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Username = QtWidgets.QLabel(self.layoutWidget)
        self.Username.setObjectName("Username")
        self.gridLayout.addWidget(self.Username, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(201, 31))
        self.lineEdit.setMaximumSize(QtCore.QSize(201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.Password = QtWidgets.QLabel(self.layoutWidget)
        self.Password.setObjectName("Password")
        self.gridLayout.addWidget(self.Password, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(201, 31))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 70, 361, 301))
        self.textBrowser.setStyleSheet("border-image: url(D:/ships_vision/Login_and_Register/image/house.jpg);")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 20, 471, 41))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        """槽函数"""
        self.Regist.clicked.connect(self.regist_button)  #跳转到注册页面
        self.re.SuccessReg.connect(self.Success_Regist)  #注册或者取消跳转回来
        self.Login.clicked.connect(self.login_button)    #登录
        self.Logout.clicked.connect(self.logout_button)  #退出

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "用户登录"))
        self.Login.setText(_translate("Form", "登录"))
        self.Logout.setText(_translate("Form", "退出"))
        self.Regist.setText(_translate("Form", "注册"))
        self.Username.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">账号</span></p></body></html>"))
        self.Password.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">密码</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; font-style:italic;\">卡口船舶识别系统</span></p></body></html>"))

        self.lineEdit.setFocus()
        self.lineEdit.setPlaceholderText("请输入账号")
        self.lineEdit_2.setPlaceholderText("请输入密码")
        self.lineEdit_2.setEchoMode(QLineEdit.Password) #密码隐藏

        # self.setFocusPolicy(Qt.StrongFocus)
    #注册
    def regist_button(self):
        #载入数据库
        # self.sql = Oper_Mysql()
        # self.sql.ZSGC_Mysql()
        self.re.show()
        widget.close()

    def search_info(self,cur, query):
        try:
            cur.execute(query)
            results = cur.fetchall()
            if results:  # 检查结果是否为空
                res = str(results[0][0])
            else:
                res = ""  # 如果结果为空，返回相应的消息
        except pymysql.Error as err:
            print(f"Error executing query: {err}")
            res = "Error executing query"  # 处理其他异常情况
        return res
    #登录
    def login_button(self):
        print("login button")
        Login_User=self.lineEdit.text()
        Login_Passwd=self.lineEdit_2.text()

        conn=db.connect_to_database()
        cur=db.create_cursor(conn)
        if Login_User == '' or Login_Passwd.strip() == '':
            # 如果非空可以进行名称匹配，否则不行
            QMessageBox.information(self, "error", "输入错误")
        else:
            print("Login_User is "+Login_User)
            query_pw=f"SELECT password FROM user_info WHERE user_name='{Login_User}'"
            query_un=f"SELECT user_name FROM user_info WHERE user_name='{Login_User}'"
            try:
                pw = self.search_info(cur, query_pw)
                un = self.search_info(cur, query_un)
                print("pw is " + pw)
                print("un is " + un)
            except Exception as e:
                print(f"Error in login_button: {e}")
            if Login_Passwd==pw and Login_User==un:
                widget.close()
                mess = QMessageBox()
                mess.setWindowTitle("Success")
                mess.setText("登录成功")
                mess.setStandardButtons(QMessageBox.Ok)
                # mess.button(QMessageBox.Ok).animateClick(1000)  # 弹框定时关闭
                mess.exec_()
                print("登录成功")

            else:
                QMessageBox.information(self, "waining", "用户名或密码错误", QMessageBox.Ok)
        db.close_connection(cur,conn)

    #退出
    def logout_button(self):
        #警告对话框
        messageBox = QMessageBox(QMessageBox.Warning, "警告", "是否退出系统！")
        Qyes = messageBox.addButton(self.tr("确认"), QMessageBox.YesRole)
        Qno = messageBox.addButton(self.tr("取消"), QMessageBox.NoRole)
        messageBox.setDefaultButton(Qno)   #默认焦点
        messageBox.exec_()   #保持
        if messageBox.clickedButton() == Qyes:
            widget.close()
        else:
            return
    #成功注册
    def Success_Regist(self):
        widget.show()
        self.re.close()


if __name__=="__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app=QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    w=Login_Ui()
    w.setupUi(widget)
    widget.show()
    sys.exit(app.exec())