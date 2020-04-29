# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Notes(object):
    def setupUi(self, Notes):
        Notes.setObjectName("Notes")
        Notes.resize(1097, 814)
        Notes.setStyleSheet("background-image: url(:/background/New folder (2)/notes background.jpg);")
        self.centralwidget = QtWidgets.QWidget(Notes)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 1081, 741))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("background-image: url(:/background/New folder (2)/notes background.jpg);")
        self.tabWidget.setObjectName("tabWidget")
        self.writenote = QtWidgets.QWidget()
        self.writenote.setObjectName("writenote")
        self.title = QtWidgets.QLineEdit(self.writenote)
        self.title.setGeometry(QtCore.QRect(740, 60, 311, 31))
        self.title.setObjectName("title")
        self.content = QtWidgets.QTextEdit(self.writenote)
        self.content.setGeometry(QtCore.QRect(70, 110, 931, 501))
        self.content.setAutoFillBackground(True)
        self.content.setObjectName("content")
        self.notetext = QtWidgets.QLabel(self.writenote)
        self.notetext.setGeometry(QtCore.QRect(600, 60, 131, 31))
        self.notetext.setText("")
        self.notetext.setPixmap(QtGui.QPixmap(":/Titles/New folder (2)/Title.png"))
        self.notetext.setObjectName("notetext")
        self.titlehere = QtWidgets.QLabel(self.writenote)
        self.titlehere.setGeometry(QtCore.QRect(0, 20, 501, 41))
        self.titlehere.setText("")
        self.titlehere.setPixmap(QtGui.QPixmap(":/Titles/New folder (2)/writeyoutnotehere.png"))
        self.titlehere.setObjectName("titlehere")
        self.savebutton = QtWidgets.QPushButton(self.writenote)
        self.savebutton.setGeometry(QtCore.QRect(490, 630, 151, 41))
        self.savebutton.setObjectName("savebutton")
        self.tabWidget.addTab(self.writenote, "")
        self.viewnote = QtWidgets.QWidget()
        self.viewnote.setObjectName("viewnote")
        self.viewnotetitle = QtWidgets.QLabel(self.viewnote)
        self.viewnotetitle.setGeometry(QtCore.QRect(20, 30, 571, 51))
        self.viewnotetitle.setText("")
        self.viewnotetitle.setPixmap(QtGui.QPixmap(":/Titles/New folder (2)/viewnoteshere.png"))
        self.viewnotetitle.setAlignment(QtCore.Qt.AlignCenter)
        self.viewnotetitle.setObjectName("viewnotetitle")
        self.shownote = QtWidgets.QLabel(self.viewnote)
        self.shownote.setGeometry(QtCore.QRect(60, 120, 971, 531))
        self.shownote.setAlignment(QtCore.Qt.AlignCenter)
        self.shownote.setObjectName("shownote")
        self.deletenote = QtWidgets.QPushButton(self.viewnote)
        self.deletenote.setGeometry(QtCore.QRect(630, 70, 191, 41))
        self.deletenote.setObjectName("deletenote")
        self.choosefile = QtWidgets.QComboBox(self.viewnote)
        self.choosefile.setGeometry(QtCore.QRect(850, 40, 191, 31))
        self.choosefile.setObjectName("choosefile")
        self.choosefile.addItem("")
        self.viewnotebutton = QtWidgets.QPushButton(self.viewnote)
        self.viewnotebutton.setGeometry(QtCore.QRect(630, 10, 191, 41))
        self.viewnotebutton.setObjectName("viewnotebutton")
        self.tabWidget.addTab(self.viewnote, "")
        Notes.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Notes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 26))
        self.menubar.setObjectName("menubar")
        Notes.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Notes)
        self.statusbar.setObjectName("statusbar")
        Notes.setStatusBar(self.statusbar)

        self.retranslateUi(Notes)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Notes)

    def retranslateUi(self, Notes):
        _translate = QtCore.QCoreApplication.translate
        Notes.setWindowTitle(_translate("Notes", "MainWindow"))
        self.content.setHtml(_translate("Notes", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffff00;\">Edit Here</span></p></body></html>"))
        self.savebutton.setText(_translate("Notes", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.writenote), _translate("Notes", "Write Notes Here"))
        self.shownote.setText(_translate("Notes", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Your Notes Will Be Shown Here</span></p></body></html>"))
        self.deletenote.setText(_translate("Notes", "Delete This Note"))
        self.choosefile.setCurrentText(_translate("Notes", "Choose Your File Here"))
        self.choosefile.setItemText(0, _translate("Notes", "Choose Your File Here"))
        self.viewnotebutton.setText(_translate("Notes", "View This Note"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.viewnote), _translate("Notes", "View Notes Here"))
import asd_rc
