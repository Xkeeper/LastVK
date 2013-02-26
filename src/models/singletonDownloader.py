# -*- coding: UTF-8 -*-

from PyQt4.QtCore import *
import shutil
import os
import urllib2
from tempfile import mkstemp
from src.tools.tags import Tag
from src.vk.vktools import VK
from src.tools.musiclib import MusicLib


class  SingletonDownload(QThread):
    def __new__(cls, creator, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonDownload, cls).__new__(cls)
            cls.instance.__init__(creator, *args, **kwargs)
        return cls.instance

    def __init__(self, creator, *args, **kwargs):
        QThread.__init__(self)
        self.creator = creator
        self.args = args
        self.kwargs = kwargs
        self.settings = QSettings()
        self.settings.beginGroup('app')
        self.vkHandle = VK()
        self.musicLibHandle = MusicLib()

    def run(self):
        try:
            current_track = self.creator.current_track
            if not 'artist' in current_track or not 'title' in current_track:
                return

            if not self.settings.contains('userVK/cookie'):
                self.setStatusLabelTextSignal.emit(u'Не авторизован ВКонтакте, проверьте настройки')
                return

            self.creator.setProgressBarValueSignal.emit(5)
            if not self.vkHandle.check_connection():
                self.creator.setStatusLabelTextSignal.emit(u'Не удается соединиться с сервером ВКонтакте')
                return

            _cookie = self.settings.value('userVK/cookie').toString()
            self.vkHandle.set_cookie(_cookie)
            if not self.vkHandle.is_logged():
                self.creator.setStatusLabelTextSignal.emit(u'Авторизационные данные ВКонтакте не корректны, проверьте настройки')
                return

            self.creator.setProgressBarValueSignal.emit(10)
            _song = self.vkHandle.search_best(current_track['artist'], current_track['title'])
            if not _song:
                self.creator.setStatusLabelTextSignal.emit(u'Трек не найден в базе ВКонтакте')
            else:
                recieved_bytes, filetmp_path = self.downloadtemp(_song['url'])
                if filetmp_path:
                    try:
                        file_tags = Tag(filetmp_path)
                    except ValueError:
                        pass
                    else:
                        file_tags.flush_tags()
                        file_tags.set_tags(**current_track)
                    song_title = u'{0} - {1}.mp3'.format(current_track['artist'], current_track['title'])
                    save_path = self.musicLibHandle.get_path()
                    if not os.path.exists(save_path):
                        os.mkdir(save_path)
                    shutil.move(filetmp_path, self.musicLibHandle.get_path() + '/' + song_title)
                    self.creator.setStatusLabelTextSignal.emit(u'Загрузка файла завершена')

                else:
                    self.creator.setStatusLabelTextSignal.emit(u'Не удалось загрузить файл')
        finally:
            self.creator.setProgressBarValueSignal.emit(0)
            self.creator.setStateDownloadButtonSignal.emit(True)

    def downloadfile(self, url, filename, dirname='.', fd=None):
        chunk_size = 40960
        file_path = os.path.join(dirname, filename)
        file_url = urllib2.urlopen(url)
        total_size = file_url.info().getheader('Content-Length').strip()
        total_size = int(total_size)
        recieved_bytes = 0
        if not fd:
            file_data = open(file_path, 'wb')
        else:
            file_data = os.fdopen(fd, 'wb')
        while True:
            chunk = file_url.read(chunk_size)
            if not chunk:
                if total_size == recieved_bytes:
                    file_data.close()
                    return recieved_bytes, file_path
                return None

            file_data.write(chunk)
            recieved_bytes += len(chunk)
            percent = (float(recieved_bytes) / float(total_size) * 90) + 10
            self.creator.setProgressBarValueSignal.emit(percent)

    def downloadtemp(self, url):
        audio_file_fd, audio_file_path = mkstemp(prefix='vkaudio', suffix='.mp3')
        audio_file_dir = os.path.dirname(audio_file_path)
        audio_file_name = os.path.basename(audio_file_path)
        recieved_bytes, file_path = self.downloadfile(url, audio_file_name,
                                                      dirname=audio_file_dir,
                                                      fd=audio_file_fd)
        if recieved_bytes and file_path:
            return recieved_bytes, file_path
        return None