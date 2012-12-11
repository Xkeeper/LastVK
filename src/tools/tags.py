from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TRCK, TIT2, TPE1, TALB, TDRC, TCON, COMM

class Tag:
    """ Class for work with ID3 tags of Mp3 files """

    def __init__( self, audio_filename ):
        """
            @type audio_filename str

            Init function of Tag class
        """
        self.filepath = audio_filename
        try:
            audio = EasyID3(audio_filename)
        except:
            raise ValueError
        else:
            self.tags = {}
            self.tags['artist'] = audio.get('artist','Unknown')
            self.tags['title'] = audio.get('title', 'Unknown')
            self.tags['album'] = audio.get('album', 'Unknown')
            self.tags['genre'] = audio.get('genre', None)
            self.tags['album_date'] = audio.get('date', None)
            self.tags['tracknumber'] = audio.get('tracknumber', None)


    def set_tags( self, **kwargs ):
        """
            @type **kwargs dict

            Set ID3 tags (artist, title, album, album_date, genre, tracknumber) in mp3 files
        """

        idTag = ID3()
        audio = {}
        audio['artist'] = kwargs.get('artist', self.tags['artist'])
        audio['title'] = kwargs.get('title', self.tags['title'])
        audio['album'] = kwargs.get('album', self.tags['album'])
        audio['album_date'] = kwargs.get('album_year', self.tags['album_date'])
        audio['genre'] = kwargs.get('genre', self.tags['genre'])
        audio['tracknumber'] = kwargs.get('tracknumber', self.tags['tracknumber'])

        idTag.add(TRCK(encoding=3, text=audio['tracknumber']))
        idTag.add(TIT2(encoding=3, text=audio['title']))
        idTag.add(TPE1(encoding=3, text=audio['artist']))
        idTag.add(TALB(encoding=3, text=audio['album']))
        idTag.add(TDRC(encoding=3, text=audio['album_date']))
        idTag.add(TCON(encoding=3, text=audio['genre']))
        try:
            idTag.save(self.filepath)

        except:
            pass


    def flush_tags( self ):
        """
            Delete all ID3 tags in mp3 files
        """
        try:
            audio = MP3(self.filepath)
            audio.delete()
            audio.save()
        except:
            pass
