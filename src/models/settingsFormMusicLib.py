# -*- coding: UTF-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from src.views.settingsFormMusicLibUI import Ui_settingsFormMusicLib

from src.tools.musiclib import MusicLib

class SettingsFormMusicLib(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_settingsFormMusicLib()
        self.ui.setupUi(self)
        self.musicLibHandle = MusicLib()
        self.settings = QSettings()
        self.settings.beginGroup('app/musiclib')
        if self.settings.contains('saveway'):
            _currentIndex, ok =  self.settings.value('saveway').toInt()
            self.ui.comboBox.setCurrentIndex(_currentIndex)

        if self.settings.contains('musiclibpath'):
            self.ui.musiclibPathEdit.setText(self.settings.value('musiclibpath').toString())
        else:
            pass

        if self.settings.contains('itunespath'):
            self.ui.iTunesMediaPathEdit.setText(self.settings.value('itunespath').toString())
        else:
            pass

    @pyqtSlot(int)
    def on_comboBox_currentIndexChanged(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

    @pyqtSlot()
    def on_musiclibPathButton_clicked(self):
        musiclibPath = QFileDialog.getExistingDirectory(self,
            u"Укажите папку для сохранения файлов",
            self.ui.musiclibPathEdit.text(),
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        if musiclibPath:
            self.ui.musiclibPathEdit.setText(musiclibPath)

    @pyqtSlot()
    def on_iTunesMediaPathButton_clicked(self):
        iTunesMediaPath = QFileDialog.getExistingDirectory(self,
            u'Укажите папку iTunes Media',
            self.ui.iTunesMediaPathEdit.text(),
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        if iTunesMediaPath:
            if self.musicLibHandle.isItunesFolder(iTunesMediaPath):
                self.ui.iTunesMediaPathEdit.setText(iTunesMediaPath)
            else:
                QMessageBox.warning(self, u'Ошибка', u'Папка не является библиотекой iTunes')

    def hideEvent(self, event):
        self.settings.setValue('saveway', self.ui.comboBox.currentIndex())
        iTunesMediaPath = self.ui.iTunesMediaPathEdit.text()
        if iTunesMediaPath:
            self.settings.setValue('itunespath', iTunesMediaPath)

        musiclibPath = self.ui.musiclibPathEdit.text()
        if musiclibPath:
            self.settings.setValue('musiclibpath', musiclibPath)


