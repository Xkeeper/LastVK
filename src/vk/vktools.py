# -*- coding: UTF-8 -*-

import requests
import urllib2
import re
import lxml.html
import os
import sys
import logging
import socket
from difflib import SequenceMatcher
from tempfile import mkstemp
from mutagen.mp3 import MP3

# stolen and adpated from <http://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile>
def resource_path(relative):

    return os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")), 'ssl',
        relative)

os.environ['REQUESTS_CA_BUNDLE'] = resource_path('cacert.pem')

logger = logging.getLogger('search_audio')
log_level = logging.DEBUG
logger.setLevel(log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class VK:

    songs_per_page = 10
    headers = { 'User-Agent': 'Opera/9.80 (S60; SymbOS; Opera Mobi/499; U; ru) Presto/2.4.18 Version/10.00' }

    #CLASS INIT

    def __init__( self ):
        self.cookie = ''
        self.userInfo = {}

    #VKONTAKTE SEARCH METHODS

    def __keysongs(self, song ):
        return song['ratio'], song['bitrate']

    def search_best( self, artist, track):
        """
            @type artist str
            @type track str

            Performs a Vkontakte audio search with best bitrate and match ratio
        """
        logger.info('search best executed')
        query  = artist + ' - ' + track
        songs = self.search(query)
        if songs:
            songsBitrated = list()
            filteredSongs = list()
            for song in songs:
                song_artist = song['artist'].lower()
                song_title = song['title'].lower()
                artist = artist.lower()
                track = track.lower()
                matcher_artist = SequenceMatcher(None, song_artist, artist)
                matcher_track = SequenceMatcher(None, song_title, track)
                average_ratio = (matcher_artist.ratio() + matcher_track.ratio()) / 2
                """
                print song_artist + ' / ' + artist
                print song_title + ' / ' + track
                print 'artist ratio: {0}'.format(matcher_artist.ratio())
                print 'track ratio: {0}'.format(matcher_track.ratio())
                print 'average ratio: {0}'.format(average_ratio)
                print '-' * 60
                """
                songBitrate = self.__get_bitrate(song['url'])
                song['bitrate'] = songBitrate
                song['ratio'] = average_ratio
                if songBitrate  >= 300 and average_ratio > 0.9:
                    return song
                songsBitrated.append(song)
            songsBitrated.sort(key = self.__keysongs, reverse = True)
            return songsBitrated[0]



    def search( self, query , offset = 0 ):

        """
            @type query str
            @type offset int

            Preforms a VKontakte music search by given query with given offset.
        """
        logger.info('search executed')
        if not self.cookie:
            return None

        songs = list()
        offset = abs( offset )

        posts = { 'act': 'search', 'al': '1', 'gid': '0', 'offset': offset, 'q': query, 'sort': '2' , 'count': '10' }

        response = requests.post( 'https://vkontakte.ru/audio', cookies = {'remixsid': self.cookie} ,
            headers = self.headers,
            data = posts,
            timeout = 1500).content.decode('cp1251')
        songs = self.parse_songs( response )

        if songs:
            return songs
        return False

    def parse_songs( self,  unparsed_songs ):

        """
            @type hash str

            Parses search results
        """
        logger.info('parse_songs executed')
        #pdb.set_trace()
        songs = list()
        unparsed_songs = unparsed_songs
        unparsed_songs = re.sub(r'<!(.*)!>','',unparsed_songs)
        unparsed_songs = lxml.html.fromstring(unparsed_songs)
        split_songs = unparsed_songs.find_class('audio fl_l')

        if split_songs:
            for idx, song in enumerate( split_songs ):
                try: #some song cannot be parsed, so we need to avoid crash with try/except
                    id_tag = song.get('id')
                    audio_id = re.search(r'-?\d+_\d+', id_tag).group(0)
                    audio_link = song.get_element_by_id('audio_info'+audio_id).value
                    audio_link = audio_link.split(',')[0]
                    audio_info = song.find_class('title_wrap fl_l')[0]
                    audio_artist = audio_info.getchildren()[0].text_content()
                    audio_title = audio_info.getchildren()[1].text_content()
                    audio_duration = song.find_class('duration fl_r')[0].text_content()
                    songs.append({
                        'id': audio_id,
                        'duration': audio_duration,
                        'url': audio_link,
                        'title': audio_title,
                        'artist': audio_artist
                    })
                except:
                    pass
                if idx >= self.songs_per_page - 1:
                    break
            if songs:
                return songs
        return False

    def __get_bitrate( self, url ):

        """
            @type url str

            Returns bitrate of track in url
        """
        logger.info('get bitrate executed')
        if url:
            try:
                audio_file_fd, audio_file_path = mkstemp(prefix = 'vkbitrate' ,suffix = '.mp3')
                audio_file = os.fdopen(audio_file_fd, 'wb')
                url_file = urllib2.urlopen(url, timeout = 800)
                audio_file.write(url_file.read(50000)) #FrameSize = Bitrate * 1000/8 * SamplesPerFrame / Frequency + IsPadding * PaddingSize
                audio_file.close()

                audio = MP3(audio_file_path)
                if audio:
                    return audio.info.bitrate / 1000
                else:
                    return 0
            except:
                os.remove(audio_file_path)
                #pdb.set_trace()
                return 0


    #VKONTAKTE AUTENTICATION METHODS

#    def __get_cookie( self ):
#
#        """
#            Returns vkontakte cookie from file
#        """
#
#        cookie = ''
#        if os.path.exists( self.cookies_dir + 'vkcookie' ):
#            file = open( self.cookies_dir + 'vkcookie' , 'r' )
#            cookie = file.read()
#            file.close()
#        if not cookie:
#            return False
#        self.cookie = cookie
#        return cookie

    def set_cookie( self, cookie ):
        self.cookie = cookie

#    def __auth_routine( self, email, password ):
#
#        """
#            Gets new cookie from vkontakte
#        """
#        response = requests.post( 'http://vk.com/login.php?op=a_login_attempt&login=' + email )
#        if not response:
#            return False
#        if response.content == 'vklogin':
#            mainpage = requests.get("http://vk.com")
#            ip_h = re.search("ip_h: '(\d|\w*)'",mainpage.content).group(1)
#            hash = re.search("hash: '(\d|\w*)'",mainpage.content).group(1)
#            posts = { 'act': 'login', 'q': '1',
#                      'al_frame': '1', 'captcha_sid' : '',
#                      'captcha_key': '', 'from_host': 'vk.com',
#                      'from_protocol': 'http',
#                      'email': email, 'pass': password,
#                      'ip_h': ip_h ,'expire': '' }
#            response = requests.post('https://login.vk.com/?act=login', posts, headers = self.headers)
#            cookie = re.search( '([0-9a-f]){55,65}', response.headers['set-cookie'] ).group(0)
#            return cookie
#        response_json = json.loads(response.content) #TODO: auth with captcha
#        return False

    def is_logged( self ):
        """
            Return True when logged in vk.com or False if not
        """
        logger.info('is_logged started')
        if self.cookie:

            mainpage = requests.get("https://m.vk.com", cookies  = {'remixsid': self.cookie} )
            parsed = lxml.html.fromstring(mainpage.content)
            if parsed.find_class('user_wrap'):
                return True
        return False

    def check_connection(self):
        logger.info('check_connection started')
        try:
            mainpage = requests.get("http://m.vk.com", timeout = 5)
        except requests.ConnectionError or socket.timeout:
            return False
        return True

    def getUser(self):
        logger.info('getUser started')
        if not self.cookie:
            return {}
        print self.cookie
        userName = ''
        try:
            mainpage = requests.get("https://m.vk.com", cookies = {'remixsid': self.cookie})
            parsed = lxml.html.fromstring(mainpage.content)
            for item in parsed.find_class('cont'):
                tag = item.find('h2')
                if tag is not None:
                    userName = tag.text
            userAvatar = parsed.find_class('user_wrap')[0].getchildren()[0].getchildren()[0].attrib['src']
        except:
            logger.error("user details not parsed")
            return {}
        self.userInfo['username'] = unicode(userName)
        self.userInfo['userimgurl'] = unicode(userAvatar)
        return self.userInfo
