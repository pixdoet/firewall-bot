# lyrical.py
# for finding a song's lyrics

from lyricsgenius import Genius
TOKEN = ('')#insert token
genius = Genius(TOKEN)

def find(inputSong,inputArtist):
    songToSearch = (inputSong,inputArtist)
    songlyrics = genius.search_song(songToSearch)
    return songlyrics.lyrics
