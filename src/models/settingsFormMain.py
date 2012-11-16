# -*- coding: UTF-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from src.views.settingsFormMainUI import Ui_settingsFormMain
from src.models.settingsFormVK import SettingsFormVK
from src.models.settingsFormLastFM import SettingsFormLastFM
from src.models.settingsFormMusicLib import SettingsFormMusicLib

class SettingsFormMain(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_settingsFormMain()
        self.ui.setupUi(self)
        self.stackedPages = {}
        self.__addActions()
        self.__addWidgets()

    def __addWidgets(self):
        self.settingsFormVKWidget = SettingsFormVK()
        self.stackedPages['settingsVK'] = self.ui.stackedWidget.addWidget(self.settingsFormVKWidget)
        self.settingsFormLastFMWidget = SettingsFormLastFM()
        self.stackedPages['settingsLastFM'] = self.ui.stackedWidget.addWidget(self.settingsFormLastFMWidget)
        self.settingsFormMusicLibWidget = SettingsFormMusicLib()
        self.stackedPages['settingsMusicLib'] = self.ui.stackedWidget.addWidget(self.settingsFormMusicLibWidget)

    def __addActions(self):
        self.settingsActionGroup = QActionGroup(self)
        self.ui.actionSettingsVK.setChecked(True)
        self.settingsActionGroup.addAction(self.ui.actionSettingsVK)
        self.settingsActionGroup.addAction(self.ui.actionSettingsLastFM)
        self.settingsActionGroup.addAction(self.ui.actionSettingsMusicLib)
        self.ui.toolBar.addActions(self.settingsActionGroup.actions())




    @pyqtSlot()
    def on_actionSettingsVK_triggered(self):
        self.ui.stackedWidget.setCurrentIndex(self.stackedPages['settingsVK'])

    @pyqtSlot()
    def on_actionSettingsLastFM_triggered(self):
        self.ui.stackedWidget.setCurrentIndex(self.stackedPages['settingsLastFM'])

    @pyqtSlot()
    def on_actionSettingsMusicLib_triggered(self):
        self.ui.stackedWidget.setCurrentIndex(self.stackedPages['settingsMusicLib'])






