# -*- coding: UTF-8 -*-

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from src.models.trayWrapper import TrayWrapper
import time

class LastVK(QApplication):
    def __init__(self):
        QApplication.__init__(self, sys.argv)
        QCoreApplication.setOrganizationName('testinc')
        QCoreApplication.setOrganizationDomain('0fh.ru')
        QCoreApplication.setApplicationName('LastVK')
        self.setQuitOnLastWindowClosed(False)
        self.trayIcon = TrayWrapper()

    def event(self, e):
        if e.type() == QEvent.ApplicationActivate:
            self.trayIcon.activateActionSignal.emit()
            return True
        return QApplication.event(self, e)

def main():
    app = LastVK()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
