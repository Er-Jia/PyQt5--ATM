# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signup1(object):
    def setupUi(self, signup1):
        signup1.setObjectName("signup1")
        signup1.resize(500, 400)
        signup1.setStyleSheet("#signup1{background-color: rgb(52, 80, 164);border-top-left-radius:15px;border-top-right-radius:5px;border-bottom-left-radius:15px;border-bottom-right-radius:5px}\n"
"")
        self.label1 = QtWidgets.QLabel(signup1)
        self.label1.setGeometry(QtCore.QRect(80, 70, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color:rgb(255, 255, 255)")
        self.label1.setScaledContents(False)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setWordWrap(False)
        self.label1.setOpenExternalLinks(False)
        self.label1.setObjectName("label1")
        self.label_2 = QtWidgets.QLabel(signup1)
        self.label_2.setGeometry(QtCore.QRect(60, 180, 161, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.signup_btn = QtWidgets.QPushButton(signup1)
        self.signup_btn.setGeometry(QtCore.QRect(360, 320, 120, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signup_btn.setFont(font)
        self.signup_btn.setStyleSheet("QPushButton{border:2px groove gray;border-radius:20px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.signup_btn.setObjectName("signup_btn")
        self.pic1 = QtWidgets.QLabel(signup1)
        self.pic1.setGeometry(QtCore.QRect(10, 0, 231, 51))
        self.pic1.setText("")
        self.pic1.setPixmap(QtGui.QPixmap(":/pics/pictures/pic1.png"))
        self.pic1.setObjectName("pic1")
        self.pwd = QtWidgets.QLineEdit(signup1)
        self.pwd.setGeometry(QtCore.QRect(210, 180, 161, 31))
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setObjectName("pwd")
        self.pwd1 = QtWidgets.QLineEdit(signup1)
        self.pwd1.setGeometry(QtCore.QRect(210, 230, 161, 31))
        self.pwd1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd1.setObjectName("pwd1")
        self.label_3 = QtWidgets.QLabel(signup1)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.account = QtWidgets.QLabel(signup1)
        self.account.setGeometry(QtCore.QRect(210, 70, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account.sizePolicy().hasHeightForWidth())
        self.account.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.account.setFont(font)
        self.account.setStyleSheet("color:rgb(255, 255, 255)")
        self.account.setText("")
        self.account.setScaledContents(False)
        self.account.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.account.setWordWrap(False)
        self.account.setOpenExternalLinks(False)
        self.account.setObjectName("account")
        self.label1_3 = QtWidgets.QLabel(signup1)
        self.label1_3.setGeometry(QtCore.QRect(70, 120, 221, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1_3.sizePolicy().hasHeightForWidth())
        self.label1_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label1_3.setFont(font)
        self.label1_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.label1_3.setScaledContents(False)
        self.label1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_3.setWordWrap(False)
        self.label1_3.setOpenExternalLinks(False)
        self.label1_3.setObjectName("label1_3")

        self.retranslateUi(signup1)
        QtCore.QMetaObject.connectSlotsByName(signup1)

    def retranslateUi(self, signup1):
        _translate = QtCore.QCoreApplication.translate
        signup1.setWindowTitle(_translate("signup1", "注册"))
        self.label1.setText(_translate("signup1", "您的账号为："))
        self.label_2.setText(_translate("signup1", "请输入密码："))
        self.signup_btn.setText(_translate("signup1", "注册"))
        self.label_3.setText(_translate("signup1", "请再次输入密码："))
        self.label1_3.setText(_translate("signup1", "请设置六位数字密码!"))
import pics_rc