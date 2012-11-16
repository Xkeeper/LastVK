# -*- coding: UTF-8 -*-

from PyQt4.QtCore import *

import urllib2
import sys
import os.path
from tempfile import mkstemp

class Downloader(QObject):
    downloadProgressSignal = pyqtSlot(int)
    def __init__(self, creator):
        QObject.__init__(self)
        self._creator = creator


    def downloadfile(self, url, filename, dirname = '.', fd = None):
        chunk_size = 40960
        file_path = dirname + '/' + filename
        file_url = urllib2.urlopen(url)
        total_size = file_url.info().getheader('Content-Length').strip()
        total_size = int(total_size)
        recieved_bytes = 0
        if not fd:
            file_data = open(file_path,'wb')
        else:
            file_data = os.fdopen(fd, 'wb')
        while True:
            chunk = file_url.read(chunk_size)
            if not chunk:
                if total_size == recieved_bytes:
                    print 'done.'
                    file_data.close()
                    return recieved_bytes, file_path
                return None

            file_data.write(chunk)
            recieved_bytes += len(chunk)
            percent = (float(recieved_bytes) / float(total_size) * 90) + 10
            self._creator.setProgressBarValueSignal.emit(percent)

    def downloadtemp(self, url):
        audio_file_fd, audio_file_path = mkstemp(prefix = 'vkaudio' ,suffix = '.mp3')
        audio_file_dir = os.path.dirname(audio_file_path)
        audio_file_name = os.path.basename(audio_file_path)
        recieved_bytes, file_path = self.downloadfile(url, audio_file_name,
            dirname = audio_file_dir,
            fd = audio_file_fd
            )
        if recieved_bytes and file_path:
            return recieved_bytes, file_path
        return None