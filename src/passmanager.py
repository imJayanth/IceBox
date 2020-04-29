# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passmanager.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PasswordManager(object):
    def setupUi(self, PasswordManager):
        PasswordManager.setObjectName("PasswordManager")
        PasswordManager.resize(1100, 836)
        PasswordManager.setStyleSheet("background-image: url(:/background/New folder (2)/passwordmanagerback.jpg);")
        self.centralwidget = QtWidgets.QWidget(PasswordManager)
        self.centralwidget.setObjectName("centralwidget")
        self.passpage = QtWidgets.QLabel(self.centralwidget)
        self.passpage.setGeometry(QtCore.QRect(310, 210, 761, 541))
        self.passpage.setAlignment(QtCore.Qt.AlignCenter)
        self.passpage.setObjectName("passpage")
        self.deletepass = QtWidgets.QPushButton(self.centralwidget)
        self.deletepass.setGeometry(QtCore.QRect(40, 410, 201, 80))
        self.deletepass.setObjectName("deletepass")
        self.createpass = QtWidgets.QPushButton(self.centralwidget)
        self.createpass.setGeometry(QtCore.QRect(40, 210, 201, 80))
        self.createpass.setObjectName("createpass")
        self.editpass = QtWidgets.QPushButton(self.centralwidget)
        self.editpass.setGeometry(QtCore.QRect(40, 310, 201, 80))
        self.editpass.setObjectName("editpass")
        self.usepass = QtWidgets.QPushButton(self.centralwidget)
        self.usepass.setGeometry(QtCore.QRect(40, 520, 201, 80))
        self.usepass.setObjectName("usepass")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(40, 10, 661, 181))
        self.title.setText("")
        self.title.setPixmap(QtGui.QPixmap(":/Titles/New folder (2)/passwordmanager.png"))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.showpass = QtWidgets.QPushButton(self.centralwidget)
        self.showpass.setGeometry(QtCore.QRect(40, 630, 201, 80))
        self.showpass.setObjectName("showpass")
        self.usefilesafe = QtWidgets.QPushButton(self.centralwidget)
        self.usefilesafe.setGeometry(QtCore.QRect(880, 30, 131, 51))
        self.usefilesafe.setObjectName("usefilesafe")
        self.usenotes = QtWidgets.QPushButton(self.centralwidget)
        self.usenotes.setGeometry(QtCore.QRect(880, 110, 131, 51))
        self.usenotes.setObjectName("usenotes")
        PasswordManager.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PasswordManager)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        PasswordManager.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PasswordManager)
        self.statusbar.setObjectName("statusbar")
        PasswordManager.setStatusBar(self.statusbar)

        self.retranslateUi(PasswordManager)
        QtCore.QMetaObject.connectSlotsByName(PasswordManager)

    def retranslateUi(self, PasswordManager):
        _translate = QtCore.QCoreApplication.translate
        PasswordManager.setWindowTitle(_translate("PasswordManager", "MainWindow"))
        self.passpage.setText(_translate("PasswordManager", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Your Passwords will be shown Here !</span></p></body></html>"))
        self.deletepass.setText(_translate("PasswordManager", "Delete a Password"))
        self.createpass.setText(_translate("PasswordManager", "Create a Password"))
        self.editpass.setText(_translate("PasswordManager", "Edit a Password"))
        self.usepass.setText(_translate("PasswordManager", "Use a Password"))
        self.showpass.setText(_translate("PasswordManager", "Show All Paswords"))
        self.usefilesafe.setText(_translate("PasswordManager", "Use FileSafe"))
        self.usenotes.setText(_translate("PasswordManager", "Use SecretNotes"))
import asd_rc
