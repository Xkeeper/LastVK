# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/qtui/settingsFormLastFM.ui'
#
# Created: Fri Nov 30 12:24:34 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_settingsFormLastFM(object):
    def setupUi(self, settingsFormLastFM):
        settingsFormLastFM.setObjectName(_fromUtf8("settingsFormLastFM"))
        settingsFormLastFM.resize(500, 145)
        self.loginLastFMButton = QtGui.QPushButton(settingsFormLastFM)
        self.loginLastFMButton.setGeometry(QtCore.QRect(160, 100, 171, 32))
        self.loginLastFMButton.setObjectName(_fromUtf8("loginLastFMButton"))
        self.groupBox = QtGui.QGroupBox(settingsFormLastFM)
        self.groupBox.setGeometry(QtCore.QRect(50, 20, 381, 61))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 16, 131, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lastFMUserNameLabel = QtGui.QLabel(self.groupBox)
        self.lastFMUserNameLabel.setGeometry(QtCore.QRect(150, 16, 221, 20))
        self.lastFMUserNameLabel.setText(_fromUtf8(""))
        self.lastFMUserNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lastFMUserNameLabel.setObjectName(_fromUtf8("lastFMUserNameLabel"))

        self.retranslateUi(settingsFormLastFM)
        QtCore.QMetaObject.connectSlotsByName(settingsFormLastFM)

    def retranslateUi(self, settingsFormLastFM):
        settingsFormLastFM.setWindowTitle(QtGui.QApplication.translate("settingsFormLastFM", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.loginLastFMButton.setText(QtGui.QApplication.translate("settingsFormLastFM", "Авторизация Last.FM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("settingsFormLastFM", "Имя пользователя:", None, QtGui.QApplication.UnicodeUTF8))

