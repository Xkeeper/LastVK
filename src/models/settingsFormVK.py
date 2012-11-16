# -*- coding: UTF-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from src.views.settingsFormVKUI import Ui_settingsFormVK
from src.models.loginVkForm import LoginVk
from src.vk.vktools import VK
from src.models.preloaderWidget import PreloaderWidget
from src.tools.threading import GenericThread

import time



class SettingsFormVK(QWidget):
    updateUIuserSignal = pyqtSignal(bool, dict)
    setPreloaderStateSignal = pyqtSignal(bool)
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_settingsFormVK()
        self.ui.setupUi(self)
        self.updateUIuserSignal.connect(self.updateUIuser)
        self.setPreloaderStateSignal.connect(self.setPreloaderState)
        self.settings = QSettings()
        self.settings.beginGroup('app')
        self.vkHandle = VK()
        cookie = unicode(self.settings.value('userVK/cookie').toString())
        if cookie:
            self.vkHandle.set_cookie(cookie)
        self.preloader = PreloaderWidget(self)
        self.updateUI()

    def updateUI(self):
        self.updateUIvk()

    def updateUIvk(self):
        userName = unicode(self.settings.value('userVK/username').toString())
        cookie = unicode(self.settings.value('userVK/cookie').toString())
        if userName and cookie:
            self.ui.userNameLabel.setText(userName)
            self.ui.logoffVkButton.setEnabled(True)
            self.ui.loginVkButton.setEnabled(False)
        else:
            self.ui.loginVkButton.setEnabled(True)
            self.ui.logoffVkButton.setEnabled(False)
        if not self.vkHandle.check_connection():
            self.ui.statusLabel.setText(u'Невозможно установить соединение')

        else:
            self.thread = GenericThread(self.getUserInfo)
            self.thread.start()

    @pyqtSlot(bool)
    def setPreloaderState(self, state):
        if state:
            self.preloader.start()
        else:
            self.preloader.stop()

    def getUserInfo(self):
        self.setPreloaderStateSignal.emit(True)
        try:
            if self.checkCookies():
                vkuser = self.vkHandle.getUser()
                if vkuser:
                    self.updateUIuserSignal.emit(True, vkuser)
                    self.setPreloaderStateSignal.emit(False)
            else:
                self.updateUIuserSignal.emit(False, {})
                self.setPreloaderStateSignal.emit(False)
        except:
            self.setPreloaderStateSignal.emit(False)

    @pyqtSlot(bool, dict)
    def updateUIuser(self, authorized, userInfo):
        if authorized:
            userName = userInfo.get('username', u'')
            self.settings.setValue('userVK/username', userName)
            self.ui.userNameLabel.setEnabled(True)
            self.ui.userNameLabel.setText(userName)
            self.ui.logoffVkButton.setEnabled(True)
            self.ui.loginVkButton.setEnabled(False)
            self.ui.statusLabel.setText(u'Авторизован')
        else:
            self.ui.userNameLabel.setEnabled(False)
            self.ui.userNameLabel.setText(u'')
            self.ui.statusLabel.setText(u'Не авторизован')
            self.ui.logoffVkButton.setEnabled(False)
            self.ui.loginVkButton.setEnabled(True)


    def checkCookies(self):
        if self.vkHandle.check_connection():
            if self.vkHandle.is_logged():
                return True
            else:
                self.flushUserInfo()
        return False

    def flushUserInfo(self):
        self.settings.setValue('userVK/username', '')
        self.settings.setValue('userVK/cookie', '')
        self.vkHandle.set_cookie('')

    @pyqtSlot(str)
    def accept_cookie(self, cookie):
        self.settings.setValue('userVK/cookie',unicode(cookie))
        self.vkHandle.set_cookie(cookie)
        self.updateUI()

    @pyqtSlot()
    def on_loginVkButton_clicked(self):
        self.loginVkWindow = LoginVk()
        self.loginVkWindow.acceptCookieSignal.connect(self.accept_cookie)
        self.loginVkWindow.show()

    @pyqtSlot()
    def on_logoffVkButton_clicked(self):
        self.flushUserInfo()
        self.updateUI()