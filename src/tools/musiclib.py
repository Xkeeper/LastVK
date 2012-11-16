from PyQt4.QtCore import *

import os
from plistlib import readPlist
from difflib import SequenceMatcher
import sys

class MusicLib(object):

    def __init__(self):
        self.settings = QSettings()
        self.settings.beginGroup('app/musiclib')
        if self.settings.contains('saveway'):
            self.saveway, ok = self.settings.value('saveway').toInt()
        else:
            self.saveway = 0
            self.settings.setValue('saveway', self.saveway)

        if self.settings.contains('itunespath'):
            self.itunes_path = unicode(self.settings.value('itunespath').toString())
        else:
            self.itunes_path = self.get_default_itunes_path()
            self.settings.setValue('itunespath', self.itunes_path)

        if self.settings.contains('musiclibpath'):
            self.musilib_path = unicode(self.settings.value('musiclibpath').toString())
        else:
            self.musilib_path = self.get_default_musiclib_path()
            self.settings.setValue('musiclibpath', self.musilib_path)

    def get_default_itunes_path(self):
        itunes_path = os.path.join(os.path.expanduser('~'), u'Music', u'iTunes') #TODO find real path to iTunes lib
        return itunes_path

    def get_default_musiclib_path(self):
        musiclib_path = os.path.join(os.path.expanduser('~'), u'Music', u'LastVK')
        return musiclib_path

    def has_itunes(self, artist, title):
        """
            @type artist str
            @type title str

            Check track in iTunes Music Library
        """
        itunes_plist = readPlist(os.path.join(self.itunes_path, u'iTunes Music Library.xml'))
        itunes_tracks = itunes_plist['Tracks']
        _artist = artist.lower()
        _title = title.lower()
        finded = False
        #TODO: Add search in itunes_autoadd_path
        for track in itunes_tracks:
            if 'Artist' in itunes_tracks[track]:
                track_artist = itunes_tracks[track]['Artist'].lower()
                track_artist_ratio = SequenceMatcher(None, track_artist, _artist).ratio()
            else:
                track_artist = None
                track_artist_ratio = 0
            if 'Name' in itunes_tracks[track]:
                track_name = itunes_tracks[track]['Name'].lower()
                track_name_ratio = SequenceMatcher(None, track_name, _title).ratio()
            else:
                track_name = None
                track_name_ratio = 0
            average_ratio = (track_artist_ratio + track_name_ratio) / 2
            if average_ratio > 0.94:
                finded = True
                return finded
        return finded
            #print u'{0} - {1}\n ratio: {2}\n Finded: {3}'.format(track_artist, track_name, average_ratio, finded)

    def has_musiclib(self, artist, title):
        finded = False
        mask = u'{0} - {1}'.format(artist, title)
        for dirname, dirnames, filenames in os.walk(self.musilib_path):
            for filename in filenames:
                file = filename.rsplit('.', 1)[0]
                ratio = SequenceMatcher(None, file, mask).ratio()
                if ratio > 0.94:
                    finded = True
        return finded


    def isItunesFolder(self, path):
        return os.path.isfile(os.path.join(path, u'iTunes Music Library.xml'))

    def get_path(self):
        if self.saveway == 0:
           return self.musilib_path
        elif self.saveway == 1:
            return self.get_itunes_autoadd_path()

    def isTrackExists(self, artist, title):
        if self.saveway == 0:
            return self.has_musiclib(artist, title)
        elif self.saveway == 1:
            return self.has_itunes(artist, title)


    def get_itunes_autoadd_path(self):
        """
           Routine to get path for itunes "Automatically Add to iTunes" dir
        @return: str
        """
        if sys.platform == 'darwin':
            return os.path.join(self.itunes_path, u'iTunes Media', u'Automatically Add to iTunes.localized')
        elif sys.platform == 'win32':
            for dirname in os.listdir(os.path.join(self.itunes_path, u'iTunes Media')):
                dirname_split = dirname.split(' ')
                if ( len(dirname_split) > 2 ) and 'iTunes' in dirname_split:
                    return os.path.join(self.itunes_path, u'iTunes Media', dirname)
