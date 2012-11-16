# -*- coding: UTF-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from src.views.settingsFormLastFMUI import Ui_settingsFormLastFM
from src.models.loginLastFMForm import LoginLastFM
from src.lastfm.lasfmtools import UserLastApi

class SettingsFormLastFM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_settingsFormLastFM()
        self.ui.setupUi(self)
        self.settings = QSettings()
        self.settings.beginGroup('app')
        self.lastFMHandle = UserLastApi()
        self.updateUILastFM()

    #LastFM SETTINGS

    @pyqtSlot(unicode)
    def checkLastFMSessionKey(self, url):
        if url.split('/')[-1] == "grantaccess":
            try:
                _session_key = self.lastFMHandle.get_session_key(self.lastFMAuthUrl)
                if _session_key:
                    self.lastFMHandle.auth(_session_key)
                    user = self.lastFMHandle.get_user()
                    if user:
                        userName = user.get_name()
                        self.settings.setValue('userLastFM/username', userName)
                        self.settings.setValue('userLastFM/sessionkey', _session_key)
            finally:
                self.loginLastFMWindow.close()
                self.updateUILastFM()

        if url.split('/')[-1] == "home":
            self.loginLastFMWindow.close()

    @pyqtSlot()
    def on_loginLastFMButton_clicked(self):
        self.loginLastFMWindow = LoginLastFM()
        self.loginLastFMWindow.show()
        self.lastFMAuthUrl = self.lastFMHandle.get_web_auth_url()
        self.loginLastFMWindow.goUrlSignal.emit(self.lastFMAuthUrl)
        self.loginLastFMWindow.getAuthUrlSignal.connect(self.checkLastFMSessionKey)

    def updateUILastFM(self):
        _userName = unicode(self.settings.value('userLastFM/username').toString())
        _sessionkey = unicode(self.settings.value('userLastFM/sessionkey').toString())
        if _userName and _sessionkey:
            self.ui.lastFMUserNameLabel.setText(_userName)