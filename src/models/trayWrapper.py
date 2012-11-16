# -*- coding: UTF-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from src.models.mainWindowForm import MainWindowForm



class TrayWrapper(QMainWindow):
    activateActionSignal = pyqtSignal()
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.mainWindow = None
        self.platform = sys.platform
        if self.platform == 'darwin':
            self.trayIcon = QSystemTrayIcon(QIcon(":icons/tray/LastVK_monochrome.png"), self)
        else:
            self.trayIcon = QSystemTrayIcon(QIcon(":icons/tray/LastVK.png"), self)
            self.trayIcon.setContextMenu(self.createMenu())
        self.trayIcon.show()
        self.trayIcon.activated.connect(self.triggeredTrayIcon)
        self.activateActionSignal.connect(self.activateActionTriggered)

    @pyqtSlot(QSystemTrayIcon.ActivationReason)
    def triggeredTrayIcon(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.mainWindow and self.mainWindow.isVisible():
                self.mainWindow.close()
            else:
                self.showMainWindow()

    def showMainWindow(self):
        self.mainWindow = MainWindowForm()
        self.mainWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.mainWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.mainWindow.setGeometry(self.getWindowPositionRec())
        self.mainWindow.show()
        self.mainWindow.activateWindow()
        self.mainWindow.setFocus()

    def getWindowPositionRec(self):
        trayRect = self.trayIcon.geometry()
        windowRect = self.mainWindow.geometry()
        desktopWidget = QDesktopWidget()
        avaliableRect = desktopWidget.availableGeometry()
        trayOrientation = self.getTrayOrientation()
        if trayOrientation == 'right':
            newPointX = avaliableRect.width() - windowRect.width() - 10
            newPointY = trayRect.center().y() - ( windowRect.height() / 2 )
        elif trayOrientation == 'left':
            newPointX = avaliableRect.x() + 10
            newPointY = trayRect.center().y() - ( windowRect.height() / 2)
        elif trayOrientation == 'down':
            newPointY = trayRect.top() - windowRect.height() - 10
            newPointX = trayRect.center().x() - (windowRect.width() / 2)
            if ( newPointX + windowRect.width() ) > avaliableRect.width():
                newPointX += avaliableRect.width() - ( newPointX + windowRect.width() )
        elif trayOrientation == 'up':
            newPointY = trayRect.bottom() + 10
            newPointX = trayRect.center().x() - (windowRect.width() / 2)
            if ( newPointX + windowRect.width() ) > avaliableRect.width():
                newPointX += avaliableRect.width() - ( newPointX + windowRect.width() )
        else:
            newPointX = avaliableRect.width() - windowRect.width() - 20
            newPointY = avaliableRect.y() + 30
        newPoint = QPoint(newPointX, newPointY)
        newRect = QRect(newPoint, QSize(windowRect.width(), windowRect.height()))
        return newRect

    def getTrayOrientation(self):
        trayRect = self.trayIcon.geometry()
        if trayRect.isEmpty():
            return None
        desktopWidget = QDesktopWidget()
        avaliableRect = desktopWidget.availableGeometry()
        if (avaliableRect.height() - trayRect.y()) < (avaliableRect.height() / 2):
            if trayRect.x() > avaliableRect.width():
                return 'right'
            elif trayRect.x() < avaliableRect.x():
                return 'left'
            else:
                return 'down'
        else:
            return 'up'

    @pyqtSlot()
    def activateActionTriggered(self):
        if not self.mainWindow or not self.mainWindow.isVisible():
            self.showMainWindow()

    @pyqtSlot()
    def activateActionExit(self):
        confirm_exit = QMessageBox.question(self, u'Подтверждение завершения LastVK',
            u"Вы действительно хотите завершить приложение LastVK?",
            QMessageBox.Ok | QMessageBox.Cancel
        )
        if confirm_exit == QMessageBox.Ok:
            qApp.quit()

    def createMenu(self):
        self.trayMenu = QMenu()
        self.activateAction = QAction(u'Открыть', self)
        self.activateAction.triggered.connect(self.activateActionTriggered)
        self.exitAction = QAction(u'Выход', self)
        self.exitAction.triggered.connect(self.activateActionExit)
        self.trayMenu.addAction(self.activateAction)
        self.trayMenu.addAction(self.exitAction)
        return self.trayMenu






