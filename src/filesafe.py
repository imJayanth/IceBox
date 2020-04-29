# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filesafe.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 800)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(:/background/New folder (2)/filesafeback.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.safetitle = QtWidgets.QLabel(self.centralwidget)
        self.safetitle.setGeometry(QtCore.QRect(240, 10, 381, 141))
        self.safetitle.setText("")
        self.safetitle.setPixmap(QtGui.QPixmap(":/Titles/New folder (2)/filesafetitle.png"))
        self.safetitle.setAlignment(QtCore.Qt.AlignCenter)
        self.safetitle.setObjectName("safetitle")
        self.addfile = QtWidgets.QPushButton(self.centralwidget)
        self.addfile.setGeometry(QtCore.QRect(50, 250, 121, 171))
        self.addfile.setFlat(False)
        self.addfile.setObjectName("addfile")
        self.filelist = QtWidgets.QLabel(self.centralwidget)
        self.filelist.setGeometry(QtCore.QRect(280, 180, 511, 511))
        self.filelist.setAutoFillBackground(False)
        self.filelist.setAlignment(QtCore.Qt.AlignCenter)
        self.filelist.setObjectName("filelist")
        self.dropfile = QtWidgets.QComboBox(self.centralwidget)
        self.dropfile.setGeometry(QtCore.QRect(830, 210, 241, 41))
        self.dropfile.setObjectName("dropfile")
        self.dropfile.addItem("")
        self.lockerimg = QtWidgets.QLabel(self.centralwidget)
        self.lockerimg.setGeometry(QtCore.QRect(660, 10, 121, 141))
        self.lockerimg.setText("")
        self.lockerimg.setPixmap(QtGui.QPixmap(":/Titles/New folder (2)/safeart.png"))
        self.lockerimg.setObjectName("lockerimg")
        self.viewfile = QtWidgets.QPushButton(self.centralwidget)
        self.viewfile.setGeometry(QtCore.QRect(880, 290, 141, 31))
        self.viewfile.setObjectName("viewfile")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 340, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.addfile.raise_()
        self.filelist.raise_()
        self.dropfile.raise_()
        self.lockerimg.raise_()
        self.safetitle.raise_()
        self.viewfile.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addfile.setText(_translate("MainWindow", "ADD A FILE"))
        self.filelist.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#499f7e;\">List of Files will be shown Here !</span></p></body></html>"))
        self.dropfile.setCurrentText(_translate("MainWindow", "View Added Files Here"))
        self.dropfile.setItemText(0, _translate("MainWindow", "View Added Files Here"))
        self.viewfile.setText(_translate("MainWindow", "View Selected File"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete Selected File"))
import asd_rc
