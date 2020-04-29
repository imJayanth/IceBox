# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1098, 716)
        LoginWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        LoginWindow.setAutoFillBackground(False)
        LoginWindow.setStyleSheet("background-image: url(:/background/New folder (2)/aasad.png);")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userLAB = QtWidgets.QLabel(self.centralwidget)
        self.userLAB.setGeometry(QtCore.QRect(240, 290, 211, 61))
        self.userLAB.setText("")
        self.userLAB.setPixmap(QtGui.QPixmap(":/Titles/New folder (2)/username.png"))
        self.userLAB.setAlignment(QtCore.Qt.AlignCenter)
        self.userLAB.setWordWrap(False)
        self.userLAB.setObjectName("userLAB")
        self.passwlab = QtWidgets.QLabel(self.centralwidget)
        self.passwlab.setGeometry(QtCore.QRect(240, 400, 211, 61))
        self.passwlab.setText("")
        self.passwlab.setPixmap(QtGui.QPixmap(":/Titles/New folder (2)/password.png"))
        self.passwlab.setAlignment(QtCore.Qt.AlignCenter)
        self.passwlab.setWordWrap(False)
        self.passwlab.setObjectName("passwlab")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(480, 300, 331, 31))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(480, 410, 331, 31))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loginbutton.setGeometry(QtCore.QRect(460, 520, 161, 61))
        self.loginbutton.setObjectName("loginbutton")
        self.signupbutton = QtWidgets.QPushButton(self.centralwidget)
        self.signupbutton.setGeometry(QtCore.QRect(710, 520, 151, 61))
        self.signupbutton.setObjectName("signupbutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 0, 781, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Titles/New folder (2)/cooltext355311937145634.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.forgotpass = QtWidgets.QPushButton(self.centralwidget)
        self.forgotpass.setGeometry(QtCore.QRect(220, 520, 161, 61))
        self.forgotpass.setObjectName("forgotpass")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 26))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login Screen"))
        self.loginbutton.setText(_translate("LoginWindow", "Login"))
        self.signupbutton.setText(_translate("LoginWindow", "SignUp"))
        self.forgotpass.setText(_translate("LoginWindow", "Forgot Password"))
import asd_rc
