# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/qtui/loginLastFMForm.ui'
#
# Created: Fri Nov 30 12:24:33 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1024, 768)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lastFMwebView = QtWebKit.QWebView(Form)
        self.lastFMwebView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.lastFMwebView.setObjectName(_fromUtf8("lastFMwebView"))
        self.gridLayout.addWidget(self.lastFMwebView, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
