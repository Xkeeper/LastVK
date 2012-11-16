# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/qtui/preloaderWidget.ui'
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

class Ui_preloaderWidgetForm(object):
    def setupUi(self, preloaderWidgetForm):
        preloaderWidgetForm.setObjectName(_fromUtf8("preloaderWidgetForm"))
        preloaderWidgetForm.resize(426, 261)
        preloaderWidgetForm.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(preloaderWidgetForm)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 36)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.loadingLabel = QtGui.QLabel(preloaderWidgetForm)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        self.loadingLabel.setFont(font)
        self.loadingLabel.setStyleSheet(_fromUtf8(""))
        self.loadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingLabel.setObjectName(_fromUtf8("loadingLabel"))
        self.verticalLayout_6.addWidget(self.loadingLabel)
        self.progressBar = QtGui.QProgressBar(preloaderWidgetForm)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_6.addWidget(self.progressBar)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)

        self.retranslateUi(preloaderWidgetForm)
        QtCore.QMetaObject.connectSlotsByName(preloaderWidgetForm)

    def retranslateUi(self, preloaderWidgetForm):
        preloaderWidgetForm.setWindowTitle(QtGui.QApplication.translate("preloaderWidgetForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.loadingLabel.setText(QtGui.QApplication.translate("preloaderWidgetForm", "Загрузка данных...", None, QtGui.QApplication.UnicodeUTF8))

