# -*- coding: UTF-8 -*-

import pylast
from datetime import datetime

class LastApiError(Exception):
    pass

class LastApiWSError(LastApiError):
    pass

class LastApiNetworkError(LastApiError):
    pass

class UserLastApi:

    API_KEY = "08ad56b2cbae9c315ef553581b0bbd5d"
    API_SECRET = "a79c27c09002862196e48322dedeeda6"

    def __init__(self):
        """
            Initialization of class UserLastApi
        """
        self.network = pylast.LastFMNetwork(api_key = self.API_KEY, api_secret = self.API_SECRET)
        self.skg = pylast.SessionKeyGenerator(self.network)
        self.user = None

    def get_web_auth_url(self):
        return self.skg.get_web_auth_url()

    def get_session_key(self, url):
        session_key = ''
        if url:
            session_key = self.skg.get_web_auth_session_key(url)
        return session_key

    def auth(self, key):
        self.network.session_key = key
        try:
            auth_user = self.network.get_authenticated_user()
            if not auth_user:
                return False
            self.user = self.network.get_user(auth_user.get_name())
            return self.user
        except pylast.WSError:
            raise LastApiWSError
        except pylast.NetworkError:
            raise LastApiNetworkError

    def get_user(self):
        return self.user

    def get_loved( self ):
        """
            Return list [{'artist': 'track_artist', 'title': 'track_title'}]

        """
        if not self.user:
            return []
        loved_tracks = self.user.get_loved_tracks()
        tracks = list()

        for loved_track in loved_tracks:
            tracks.append({'artist': loved_track[0].get_artist().get_name(),
                           'title': loved_track[0].get_name()
            })
            #	print u'{0} - {1}'.format(loved_track[0].get_artist().get_name(), loved_track[0].get_name())
        return tracks

    def get_playnow ( self ):
        """
            Return dict "{'artist': 'track_artist', 'title': 'track_title'}"

        """
        if not self.user:
            return {}
        track = self.user.get_now_playing()
        if track:
            playnow = {'artist': unicode(track.get_artist().get_name()),
                       'title': unicode(track.get_name())
            }
            track_top_tags = track.get_top_tags()
            if track_top_tags:
                track_genre = track_top_tags[0][0].name
                if track_genre:
                    playnow['genre'] = track_genre
            track_album = track.get_album()
            if track_album:
                playnow['album'] = track_album.get_title()
                try:
                    track_album_date = track_album.get_release_date()
                    if track_album_date:
                        date = datetime.strptime(track_album_date, '%d %b %Y, %H:%M')
                        playnow['album_year'] = str(date.year)
                except:
                    pass
            return playnow
