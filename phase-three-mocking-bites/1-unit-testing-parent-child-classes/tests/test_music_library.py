import pytest
from lib.music_library import *
from unittest.mock import Mock

def test_add_two_tracks():
    library = MusicLibrary()

    fake_track_1 = Mock()
    fake_track_1.title = "Always The Hard Way"
    fake_track_1.artist = "Terror"

    fake_track_2 = Mock()
    fake_track_2.title = "Higher Place"
    fake_track_2.artist = "Malevolence"

    library.add(fake_track_1)
    library.add(fake_track_2)

    result = library.all_tracks
    assert result == [fake_track_1, fake_track_2]

def test_search_matches_one_title():
    library = MusicLibrary()

    fake_track_1 = Mock()
    fake_track_1.title = "Always The Hard Way"
    fake_track_1.artist = "Terror"
    fake_track_1.matches.return_value = True

    fake_track_2 = Mock()
    fake_track_2.title = "Higher Place"
    fake_track_2.artist = "Malevolence"
    fake_track_2.matches.return_value = False

    library.add(fake_track_1)
    library.add(fake_track_2)

    assert library.search("Way") == [fake_track_1]

def test_search_matches_one_artist():
    library = MusicLibrary()

    fake_track_1 = Mock()
    fake_track_1.title = "Always The Hard Way"
    fake_track_1.artist = "Terror"
    fake_track_1.matches.return_value = True

    fake_track_2 = Mock()
    fake_track_2.title = "Higher Place"
    fake_track_2.artist = "Malevolence"
    fake_track_2.matches.return_value = False

    library.add(fake_track_1)
    library.add(fake_track_2)

    assert library.search("Terror") == [fake_track_1]

def test_search_matches_none():
    library = MusicLibrary()

    fake_track_1 = Mock()
    fake_track_1.title = "Always The Hard Way"
    fake_track_1.artist = "Terror"
    fake_track_1.matches.return_value = False

    fake_track_2 = Mock()
    fake_track_2.title = "Higher Place"
    fake_track_2.artist = "Malevolence"
    fake_track_2.matches.return_value = False

    library.add(fake_track_1)
    library.add(fake_track_2)

    assert library.search("Life") == []

def test_search_matches_all_titles():
    library = MusicLibrary()

    fake_track_1 = Mock()
    fake_track_1.title = "Always The Hard Way"
    fake_track_1.artist = "Terror"
    fake_track_1.matches.return_value = True

    fake_track_2 = Mock()
    fake_track_2.title = "The Higher Place"
    fake_track_2.artist = "Malevolence"
    fake_track_2.matches.return_value = True

    fake_track_3 = Mock()
    fake_track_3.title = "The Cat"
    fake_track_3.artist = "Evil"
    fake_track_3.matches.return_value = True

    library.add(fake_track_1)
    library.add(fake_track_2)
    library.add(fake_track_3)

    assert library.search("The") == [fake_track_1, fake_track_2, fake_track_3]

def test_search_matches_all_artists():
    library = MusicLibrary()

    fake_track_1 = Mock()
    fake_track_1.title = "Always The Hard Way"
    fake_track_1.artist = "Singer"
    fake_track_1.matches.return_value = True

    fake_track_2 = Mock()
    fake_track_2.title = "The Higher Place"
    fake_track_2.artist = "Singer"
    fake_track_2.matches.return_value = True

    fake_track_3 = Mock()
    fake_track_3.title = "The Cat"
    fake_track_3.artist = "Singer"
    fake_track_3.matches.return_value = True

    library.add(fake_track_1)
    library.add(fake_track_2)
    library.add(fake_track_3)

    assert library.search("Singer") == [fake_track_1, fake_track_2, fake_track_3]

def test_search_matches_multiple_titles_and_artists():
    library = MusicLibrary()

    fake_track_1 = Mock()
    fake_track_1.title = "Always The Hard Way"
    fake_track_1.artist = "Terror"
    fake_track_1.matches.return_value = True
    

    fake_track_2 = Mock()
    fake_track_2.title = "Higher Place"
    fake_track_2.artist = "Malevolence"
    fake_track_2.matches.return_value = False


    fake_track_3 = Mock()
    fake_track_3.title = "The Cat"
    fake_track_3.artist = "Evil"
    fake_track_3.matches.return_value = True


    fake_track_4 = Mock()
    fake_track_4.title = "Superheroes"
    fake_track_4.artist = "The Script"
    fake_track_4.matches.return_value = True


    fake_track_5 = Mock()
    fake_track_5.title = "Thriller"
    fake_track_5.artist = "Michael Jackson"
    fake_track_5.matches.return_value = False


    fake_track_6 = Mock()
    fake_track_6.title = "Glad You Came"
    fake_track_6.artist = "The Wanted"
    fake_track_6.matches.return_value = True


    library.add(fake_track_1)
    library.add(fake_track_2)
    library.add(fake_track_3)
    library.add(fake_track_4)
    library.add(fake_track_5)
    library.add(fake_track_6)

    assert library.search("The") == [fake_track_1, fake_track_3, fake_track_4, fake_track_6]