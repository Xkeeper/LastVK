# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/qtui/mainWindowForm.ui'
#
# Created: Thu Nov 15 13:45:41 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName(_fromUtf8("MainForm"))
        MainForm.resize(427, 166)
        self.horizontalLayoutWidget = QtGui.QWidget(MainForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 411, 151))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mainFrame = QtGui.QFrame(self.horizontalLayoutWidget)
        self.mainFrame.setEnabled(True)
        self.mainFrame.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #d1d1d1;\n"
"background-color: rgb(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(55,55,62,100);\n"
"border: 1px solid #303029;\n"
"border-radius: 10px;\n"
"color: #d1d1d1;\n"
"}\n"
"QPushButton:hover{\n"
"border: 1px solid #909099;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(48,48,48,92%);\n"
"border: 2px solid #292929;\n"
"color: #a1a1a1;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: rgb(94, 94, 94)\n"
"}\n"
"\n"
"#mainFrame{\n"
"background-color: rgb(50,50,52,98%);\n"
"border-radius: 31px;\n"
"}\n"
""))
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.downloadButton = QtGui.QPushButton(self.mainFrame)
        self.downloadButton.setEnabled(False)
        self.downloadButton.setGeometry(QtCore.QRect(140, 50, 110, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet(_fromUtf8(""))
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.downloadProgressBar = QtGui.QProgressBar(self.mainFrame)
        self.downloadProgressBar.setEnabled(True)
        self.downloadProgressBar.setGeometry(QtCore.QRect(20, 90, 341, 23))
        self.downloadProgressBar.setProperty("value", 0)
        self.downloadProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.downloadProgressBar.setTextVisible(False)
        self.downloadProgressBar.setObjectName(_fromUtf8("downloadProgressBar"))
        self.updateCycleLabel = QtGui.QLabel(self.mainFrame)
        self.updateCycleLabel.setGeometry(QtCore.QRect(50, 90, 32, 32))
        self.updateCycleLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.updateCycleLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.updateCycleLabel.setText(_fromUtf8(""))
        self.updateCycleLabel.setObjectName(_fromUtf8("updateCycleLabel"))
        self.settingsButton = QtGui.QPushButton(self.mainFrame)
        self.settingsButton.setGeometry(QtCore.QRect(370, 75, 24, 24))
        self.settingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.settingsButton.setStatusTip(_fromUtf8(""))
        self.settingsButton.setStyleSheet(_fromUtf8("#settingsButton{\n"
"border: 0;\n"
"image: url(:/buttons/mainwindow/settings.png)\n"
"}\n"
"#settingsButton:hover{\n"
"image: url(:/buttons/mainwindow/settings_on.png)\n"
"}"))
        self.settingsButton.setText(_fromUtf8(""))
        self.settingsButton.setIconSize(QtCore.QSize(24, 24))
        self.settingsButton.setObjectName(_fromUtf8("settingsButton"))
        self.statusLabel = QtGui.QLabel(self.mainFrame)
        self.statusLabel.setGeometry(QtCore.QRect(20, 120, 341, 20))
        self.statusLabel.setStyleSheet(_fromUtf8(""))
        self.statusLabel.setText(_fromUtf8(""))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.alreadyLabel = QtGui.QLabel(self.mainFrame)
        self.alreadyLabel.setGeometry(QtCore.QRect(370, 10, 24, 24))
        self.alreadyLabel.setText(_fromUtf8(""))
        self.alreadyLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/label/ok_off.png")))
        self.alreadyLabel.setScaledContents(True)
        self.alreadyLabel.setObjectName(_fromUtf8("alreadyLabel"))
        self.exitButton = QtGui.QPushButton(self.mainFrame)
        self.exitButton.setGeometry(QtCore.QRect(370, 115, 24, 24))
        self.exitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exitButton.setStyleSheet(_fromUtf8("#exitButton{\n"
"border: 0;\n"
"image: url(:/buttons/mainwindow/exit.png);\n"
"}\n"
"#exitButton:hover{\n"
"image: url(:/buttons/mainwindow/exit_on.png);\n"
"}"))
        self.exitButton.setText(_fromUtf8(""))
        self.exitButton.setIconSize(QtCore.QSize(24, 24))
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.scrollArea = QtGui.QScrollArea(self.mainFrame)
        self.scrollArea.setGeometry(QtCore.QRect(20, 10, 340, 28))
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setStyleSheet(_fromUtf8("border: 1px solid #303029;\n"
"border-radius: 10px;\n"
"background-color: rgb(50,50,52,100%)"))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 680, 28))
        self.scrollAreaWidgetContents.setStyleSheet(_fromUtf8(""))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.playNowLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.playNowLabel.setGeometry(QtCore.QRect(0, 0, 340, 28))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.playNowLabel.setFont(font)
        self.playNowLabel.setStyleSheet(_fromUtf8(""))
        self.playNowLabel.setText(_fromUtf8(""))
        self.playNowLabel.setScaledContents(False)
        self.playNowLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playNowLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.playNowLabel.setObjectName(_fromUtf8("playNowLabel"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.mainFrame)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtGui.QApplication.translate("MainForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadButton.setText(QtGui.QApplication.translate("MainForm", "Скачать", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsButton.setToolTip(QtGui.QApplication.translate("MainForm", "Настройки", None, QtGui.QApplication.UnicodeUTF8))
        self.exitButton.setToolTip(QtGui.QApplication.translate("MainForm", "Выйти", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
