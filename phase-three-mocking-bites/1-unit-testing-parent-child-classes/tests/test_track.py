import pytest
from lib.track import *

def test_initialisation():
    song = Track("Thriller", "Michael Jackson")
    result = [song.title, song.artist]
    assert result == ["Thriller", "Michael Jackson"]

def test_matches_title():
    song = Track("Thriller", "Michael Jackson")
    result = song.matches("Thriller")
    assert result == True

def test_matches_artist():
    song = Track("Thriller", "Michael Jackson")
    result = song.matches("Jackson")
    assert result == True

def test_matches_none():
    song = Track("Thriller", "Michael Jackson")
    result = song.matches("Madonna")
    assert result == False

