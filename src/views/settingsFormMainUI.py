# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/qtui/settingsFormMain.ui'
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

class Ui_settingsFormMain(object):
    def setupUi(self, settingsFormMain):
        settingsFormMain.setObjectName(_fromUtf8("settingsFormMain"))
        settingsFormMain.resize(500, 210)
        settingsFormMain.setMinimumSize(QtCore.QSize(500, 210))
        settingsFormMain.setMaximumSize(QtCore.QSize(500, 210))
        self.centralwidget = QtGui.QWidget(settingsFormMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 500, 180))
        self.stackedWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        settingsFormMain.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(settingsFormMain)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        self.toolBar.setIconSize(QtCore.QSize(40, 40))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        settingsFormMain.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSettingsVK = QtGui.QAction(settingsFormMain)
        self.actionSettingsVK.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/settings/vkontakte_button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsVK.setIcon(icon)
        self.actionSettingsVK.setObjectName(_fromUtf8("actionSettingsVK"))
        self.actionSettingsLastFM = QtGui.QAction(settingsFormMain)
        self.actionSettingsLastFM.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/settings/lastfm_button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsLastFM.setIcon(icon1)
        self.actionSettingsLastFM.setObjectName(_fromUtf8("actionSettingsLastFM"))
        self.actionSettingsMusicLib = QtGui.QAction(settingsFormMain)
        self.actionSettingsMusicLib.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/settings/musiclib_button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettingsMusicLib.setIcon(icon2)
        self.actionSettingsMusicLib.setObjectName(_fromUtf8("actionSettingsMusicLib"))

        self.retranslateUi(settingsFormMain)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(settingsFormMain)

    def retranslateUi(self, settingsFormMain):
        settingsFormMain.setWindowTitle(QtGui.QApplication.translate("settingsFormMain", "Настройки LastVK", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("settingsFormMain", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettingsVK.setText(QtGui.QApplication.translate("settingsFormMain", "ВКонтакте", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettingsLastFM.setText(QtGui.QApplication.translate("settingsFormMain", "LastFM", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettingsMusicLib.setText(QtGui.QApplication.translate("settingsFormMain", "Настройки сохранения", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
