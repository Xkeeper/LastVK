# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/qtui/settingsFormMusicLib.ui'
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

class Ui_settingsFormMusicLib(object):
    def setupUi(self, settingsFormMusicLib):
        settingsFormMusicLib.setObjectName(_fromUtf8("settingsFormMusicLib"))
        settingsFormMusicLib.resize(500, 145)
        self.stackedWidget = QtGui.QStackedWidget(settingsFormMusicLib)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 50, 501, 80))
        self.stackedWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.groupBox = QtGui.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(15, 0, 470, 81))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 161, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.musiclibPathEdit = QtGui.QLineEdit(self.groupBox)
        self.musiclibPathEdit.setGeometry(QtCore.QRect(190, 30, 231, 22))
        self.musiclibPathEdit.setMouseTracking(False)
        self.musiclibPathEdit.setFocusPolicy(QtCore.Qt.TabFocus)
        self.musiclibPathEdit.setAcceptDrops(True)
        self.musiclibPathEdit.setObjectName(_fromUtf8("musiclibPathEdit"))
        self.musiclibPathButton = QtGui.QToolButton(self.groupBox)
        self.musiclibPathButton.setGeometry(QtCore.QRect(420, 30, 27, 22))
        self.musiclibPathButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.musiclibPathButton.setObjectName(_fromUtf8("musiclibPathButton"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.page_2)
        self.groupBox_2.setGeometry(QtCore.QRect(15, 0, 470, 80))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 131, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.iTunesMediaPathEdit = QtGui.QLineEdit(self.groupBox_2)
        self.iTunesMediaPathEdit.setGeometry(QtCore.QRect(190, 30, 241, 22))
        self.iTunesMediaPathEdit.setFocusPolicy(QtCore.Qt.TabFocus)
        self.iTunesMediaPathEdit.setObjectName(_fromUtf8("iTunesMediaPathEdit"))
        self.iTunesMediaPathButton = QtGui.QToolButton(self.groupBox_2)
        self.iTunesMediaPathButton.setGeometry(QtCore.QRect(430, 30, 27, 22))
        self.iTunesMediaPathButton.setObjectName(_fromUtf8("iTunesMediaPathButton"))
        self.stackedWidget.addWidget(self.page_2)
        self.label_2 = QtGui.QLabel(settingsFormMusicLib)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 91, 26))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(settingsFormMusicLib)
        self.comboBox.setGeometry(QtCore.QRect(180, 10, 271, 26))
        self.comboBox.setFocusPolicy(QtCore.Qt.TabFocus)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))

        self.retranslateUi(settingsFormMusicLib)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(settingsFormMusicLib)
        settingsFormMusicLib.setTabOrder(self.comboBox, self.iTunesMediaPathEdit)
        settingsFormMusicLib.setTabOrder(self.iTunesMediaPathEdit, self.iTunesMediaPathButton)
        settingsFormMusicLib.setTabOrder(self.iTunesMediaPathButton, self.musiclibPathEdit)
        settingsFormMusicLib.setTabOrder(self.musiclibPathEdit, self.musiclibPathButton)

    def retranslateUi(self, settingsFormMusicLib):
        settingsFormMusicLib.setWindowTitle(QtGui.QApplication.translate("settingsFormMusicLib", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("settingsFormMusicLib", "Папка для сохранения:", None, QtGui.QApplication.UnicodeUTF8))
        self.musiclibPathButton.setText(QtGui.QApplication.translate("settingsFormMusicLib", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("settingsFormMusicLib", "Путь к папке iTunes:", None, QtGui.QApplication.UnicodeUTF8))
        self.iTunesMediaPathButton.setText(QtGui.QApplication.translate("settingsFormMusicLib", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("settingsFormMusicLib", "Сохранять в:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("settingsFormMusicLib", "Папку", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("settingsFormMusicLib", "Базу iTunes", None, QtGui.QApplication.UnicodeUTF8))

