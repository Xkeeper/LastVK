# -*- coding: UTF-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from src.tools.musiclib import MusicLib
from src.tools.threading import GenericThread
from src.views.mainWindowFormUI import Ui_MainForm
from src.models.settingsFormMain import SettingsFormMain
from src.lastfm.lasfmtools import UserLastApi, LastApiWSError, LastApiNetworkError
from singletonDownloader import SingletonDownload


class MainWindowForm(QMainWindow):
    startAnimationSignal = pyqtSignal()
    stopAnimationSignal = pyqtSignal()
    setStateDownloadButtonSignal = pyqtSignal(bool)
    setStateAlreadyLabelSignal = pyqtSignal(bool)
    setProgressBarValueSignal = pyqtSignal(int)
    setStatusLabelTextSignal = pyqtSignal(unicode)
    setPlayNowLabelTextSignal = pyqtSignal(unicode)
    abortAndShowErrorSignal = pyqtSignal(unicode)
    setUpdatePlayNowIntervalSignal = pyqtSignal(int)
    updatePlayNowInterval = 15000

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)
        self.lastFMHandle = UserLastApi()
        self.musicLibHandle = MusicLib()
        self.singletonDownloader = SingletonDownload(self)
        self.settings = QSettings()
        self.settings.beginGroup('app')
        self.lastFMUser = ''
        self.current_track = {}
        self.scrollLabelTimer = QTimer()
        self.scrollLabelTimer.setInterval(50)
        self.updatePlayNowTimer = QTimer()
        self.updatePlayNowTimer.setInterval(self.updatePlayNowInterval)
        self.loadingAnimGif = QMovie(":/animations/loading.gif")
        self.loadingAnimGif.setScaledSize(QSize(24, 24))
        self.startAnimationSignal.connect(self.start_animation)
        self.stopAnimationSignal.connect(self.stop_animation)
        self.setStateDownloadButtonSignal.connect(self.setStateDownloadButton)
        self.setProgressBarValueSignal.connect(self.setProgressBarValue)
        self.setStatusLabelTextSignal.connect(self.setStatusLabelText)
        self.setStateAlreadyLabelSignal.connect(self.setStateAlreadyLabel)
        self.setPlayNowLabelTextSignal.connect(self.setPlayNowLabelText)
        self.abortAndShowErrorSignal.connect(self.abortAndShowError)
        self.scrollLabelTimer.timeout.connect(self.on_timer_timeout)
        self.updatePlayNowTimer.timeout.connect(self.mainthread_wrapper)
        self.setUpdatePlayNowIntervalSignal.connect(self.setUpdatePlayNowInterval)
        self.updatePlayNowTimer.timeout.emit()
        self.updatePlayNowTimer.start()
        QObject.installEventFilter(self, self)

    @pyqtSlot()
    def mainthread_wrapper(self):
        self.thread = GenericThread(self.thread_func)
        self.thread.start()

    def thread_func(self):
        self.startAnimationSignal.emit()
        self.setStatusLabelTextSignal.emit(u' ')
        self.setStateAlreadyLabelSignal.emit(False)
        self.current_track = {}
        self.setStateDownloadButtonSignal.emit(False)
        self.check_current_lastfm_track()

    def check_current_lastfm_track(self):
        if not self.settings.contains('userLastFM/sessionkey'):
            self.abortAndShowErrorSignal.emit(u'Не авторизован в Last.FM, проверьте настройки')
            return
        try:
            if not self.lastFMUser:
                session_key = unicode(self.settings.value('userLastFM/sessionkey').toString())
                self.lastFMUser = self.lastFMHandle.auth(session_key)

        except LastApiWSError:
            self.abortAndShowErrorSignal.emit(u'Не удалось авторизоваться в Last.FM')
            return

        except LastApiNetworkError:
            self.abortAndShowErrorSignal.emit(u'Не удалось установить соединение с сервером')
            return

        _current_track = self.lastFMHandle.get_playnow()
        #print _current_track
        if _current_track:
            self.current_track = _current_track
            song_title = self.current_track['artist'] + ' - ' + self.current_track['title']
            self.stopAnimationSignal.emit()
            self.setPlayNowLabelTextSignal.emit(song_title)
            self.setUpdatePlayNowIntervalSignal.emit(self.updatePlayNowInterval)
            if self.musicLibHandle.isTrackExists(self.current_track['artist'], self.current_track['title']):
                self.setStateAlreadyLabelSignal.emit(True)
            else:
                self.setStateDownloadButtonSignal.emit(True)

        else:
            self.setUpdatePlayNowIntervalSignal.emit(self.updatePlayNowInterval / 4)
            self.stopAnimationSignal.emit()
            self.setStatusLabelTextSignal.emit(u'В данный момент нет проигрываемых треков')

    @pyqtSlot(unicode)
    def abortAndShowError(self, text):
        self.stopAnimationSignal.emit()
        self.current_track = {}
        self.setStatusLabelTextSignal.emit(text)

    @pyqtSlot()
    def start_animation(self):
        self.resetScrollArea()
        self.ui.playNowLabel.setMovie(self.loadingAnimGif)
        self.loadingAnimGif.start()

    @pyqtSlot()
    def stop_animation(self):
        self.loadingAnimGif.stop()
        self.loadingAnimGif.jumpToFrame(0)
        self.setPlayNowLabelTextSignal.emit(u' ')

    @pyqtSlot(unicode)
    def setPlayNowLabelText(self, text):
        self.ui.playNowLabel.setText(text)
        _font = self.ui.playNowLabel.font()
        _fm = QFontMetrics(_font)
        _str_width = _fm.width(self.ui.playNowLabel.text())
        scrollAreaWidth = self.ui.scrollArea.width()
        if _str_width > scrollAreaWidth:
            self.startScrollArea(_str_width + 10)

    @pyqtSlot(unicode)
    def setStatusLabelText(self, text):
        self.ui.statusLabel.setText(text)

    @pyqtSlot(int)
    def setProgressBarValue(self, num):
        self.ui.downloadProgressBar.setValue(num)

    @pyqtSlot(bool)
    def setStateDownloadButton(self, state):
        self.ui.downloadButton.setEnabled(state)

    @pyqtSlot(bool)
    def setStateAlreadyLabel(self, state):
        if state:
            pixmap = QPixmap(':/icons/label/ok.png')
            self.ui.alreadyLabel.setPixmap(pixmap.scaled(24, 24))
            self.ui.alreadyLabel.setToolTip(u'Трек уже есть в музыкальной библиотеке')
        else:
            pixmap = QPixmap(':/icons/label/ok_off.png')
            self.ui.alreadyLabel.setPixmap(pixmap.scaled(24, 24))

    @pyqtSlot()
    def on_settingsButton_clicked(self):
        self.settingsForm = SettingsFormMain()
        self.settingsForm.show()

    @pyqtSlot()
    def on_actionPreferences_triggered(self):
        self.on_settingsButton_clicked()

    @pyqtSlot()
    def on_downloadButton_clicked(self):
        self.setStateDownloadButtonSignal.emit(False)
        self.singletonDownloader.start()

    @pyqtSlot()
    def on_exitButton_clicked(self):
        confirm_exit = QMessageBox.question(self, u'Подтверждение завершения LastVK',
            u"Вы действительно хотите завершить приложение LastVK?",
            QMessageBox.Ok | QMessageBox.Cancel
        )
        if confirm_exit == QMessageBox.Ok:
            qApp.quit()

    @pyqtSlot()
    def on_timer_timeout(self):
        _value = self.ui.scrollArea.horizontalScrollBar().value()
        if _value >= self.__maxscroll:
            _value = -self.__scrollWidth
        self.ui.scrollArea.horizontalScrollBar().setValue(_value + 3)

    @pyqtSlot(int)
    def setUpdatePlayNowInterval(self, interval):
        self.updatePlayNowTimer.setInterval(interval)

    def resetScrollArea(self):
        self.scrollLabelTimer.stop()
        _scrollWidth = self.ui.scrollArea.width()
        self.ui.playNowLabel.setFixedWidth(_scrollWidth)
        self.ui.playNowLabel.setAlignment(Qt.AlignHCenter)
        self.ui.scrollArea.horizontalScrollBar().setValue(0)

    def startScrollArea(self, width):
        self.__scrollWidth = self.ui.scrollArea.width()
        self.__maxscroll = width
        self.ui.playNowLabel.setFixedWidth(width)
        self.ui.scrollArea.horizontalScrollBar().setMinimum(-self.__scrollWidth)
        self.ui.scrollArea.horizontalScrollBar().setMaximum(width)
        self.scrollLabelTimer.start()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.WindowDeactivate:
            if QApplication.focusWidget() == self:
                self.close()
            return True
        else:
            return QObject.eventFilter(self, obj, event)

    def closeEvent(self, event):
        self.updatePlayNowTimer.stop()
        self.scrollLabelTimer.stop()
