import pytest
from lib.track_list import *

def test_add_one_track():
    songs = TrackList()
    songs.addSong("Michael Jackson - Thriller")
    result = songs.tracks
    assert result == ["Michael Jackson - Thriller"]

def test_add_three_track():
    songs = TrackList()
    songs.addSong("Michael Jackson - Thriller")
    songs.addSong("Michael Jackson - Beat It")
    songs.addSong("Michael Jackson - Billie Jean")
    result = songs.tracks
    assert result == ["Michael Jackson - Thriller", "Michael Jackson - Beat It", "Michael Jackson - Billie Jean"]


def test_display_songs():
    songs = TrackList()
    songs.addSong("Michael Jackson - Thriller")
    songs.addSong("Michael Jackson - Beat It")
    songs.addSong("Michael Jackson - Billie Jean")
    result = songs.displaySongs()
    assert result == ["Michael Jackson - Thriller", "Michael Jackson - Beat It", "Michael Jackson - Billie Jean"]

def test_add_empty_string():
    songs = TrackList()
    with pytest.raises(Exception) as e:
        songs.addSong("")
    error_message = str(e.value)
    assert error_message == "No song name provided!"