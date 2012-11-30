# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/qtui/settingsFormVK.ui'
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

class Ui_settingsFormVK(object):
    def setupUi(self, settingsFormVK):
        settingsFormVK.setObjectName(_fromUtf8("settingsFormVK"))
        settingsFormVK.resize(500, 145)
        self.logoffVkButton = QtGui.QPushButton(settingsFormVK)
        self.logoffVkButton.setEnabled(False)
        self.logoffVkButton.setGeometry(QtCore.QRect(280, 100, 131, 32))
        self.logoffVkButton.setObjectName(_fromUtf8("logoffVkButton"))
        self.loginVkButton = QtGui.QPushButton(settingsFormVK)
        self.loginVkButton.setGeometry(QtCore.QRect(90, 100, 131, 32))
        self.loginVkButton.setObjectName(_fromUtf8("loginVkButton"))
        self.groupBox = QtGui.QGroupBox(settingsFormVK)
        self.groupBox.setGeometry(QtCore.QRect(50, 20, 401, 71))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.statusLabel = QtGui.QLabel(self.groupBox)
        self.statusLabel.setEnabled(False)
        self.statusLabel.setGeometry(QtCore.QRect(160, 40, 241, 20))
        self.statusLabel.setText(_fromUtf8(""))
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 61, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.userNameLabel = QtGui.QLabel(self.groupBox)
        self.userNameLabel.setEnabled(False)
        self.userNameLabel.setGeometry(QtCore.QRect(160, 10, 241, 20))
        self.userNameLabel.setText(_fromUtf8(""))
        self.userNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userNameLabel.setObjectName(_fromUtf8("userNameLabel"))

        self.retranslateUi(settingsFormVK)
        QtCore.QMetaObject.connectSlotsByName(settingsFormVK)

    def retranslateUi(self, settingsFormVK):
        settingsFormVK.setWindowTitle(QtGui.QApplication.translate("settingsFormVK", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.logoffVkButton.setText(QtGui.QApplication.translate("settingsFormVK", "Выйти", None, QtGui.QApplication.UnicodeUTF8))
        self.loginVkButton.setText(QtGui.QApplication.translate("settingsFormVK", "Авторизоваться", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("settingsFormVK", "Имя пользователя:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("settingsFormVK", "Статус:", None, QtGui.QApplication.UnicodeUTF8))

