# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signuppage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignupWindow(object):
    def setupUi(self, SignupWindow):
        SignupWindow.setObjectName("SignupWindow")
        SignupWindow.resize(1100, 750)
        SignupWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        SignupWindow.setStyleSheet("background-image: url(:/background/New folder (2)/signup background.jpg);")
        self.centralwidget = QtWidgets.QWidget(SignupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SignupTitle = QtWidgets.QLabel(self.centralwidget)
        self.SignupTitle.setGeometry(QtCore.QRect(420, 10, 261, 71))
        self.SignupTitle.setText("")
        self.SignupTitle.setPixmap(QtGui.QPixmap(":/Titles/New folder (2)/signup.png"))
        self.SignupTitle.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SignupTitle.setObjectName("SignupTitle")
        self.SignupValues = QtWidgets.QLabel(self.centralwidget)
        self.SignupValues.setGeometry(QtCore.QRect(260, 90, 171, 461))
        self.SignupValues.setText("")
        self.SignupValues.setPixmap(QtGui.QPixmap(":/Titles/New folder (2)/Signup labels.png"))
        self.SignupValues.setWordWrap(True)
        self.SignupValues.setObjectName("SignupValues")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(480, 150, 341, 31))
        self.name.setObjectName("name")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(480, 230, 341, 31))
        self.email.setObjectName("email")
        self.phno = QtWidgets.QLineEdit(self.centralwidget)
        self.phno.setGeometry(QtCore.QRect(480, 320, 341, 31))
        self.phno.setObjectName("phno")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(480, 390, 341, 31))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(480, 460, 341, 31))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.signup = QtWidgets.QPushButton(self.centralwidget)
        self.signup.setGeometry(QtCore.QRect(480, 640, 151, 51))
        self.signup.setObjectName("signup")
        SignupWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SignupWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        SignupWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SignupWindow)
        self.statusbar.setObjectName("statusbar")
        SignupWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SignupWindow)
        QtCore.QMetaObject.connectSlotsByName(SignupWindow)

    def retranslateUi(self, SignupWindow):
        _translate = QtCore.QCoreApplication.translate
        SignupWindow.setWindowTitle(_translate("SignupWindow", "MainWindow"))
        self.signup.setText(_translate("SignupWindow", "Sign Up"))
import asd_rc
