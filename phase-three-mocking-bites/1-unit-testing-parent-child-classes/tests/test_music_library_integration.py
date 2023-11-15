import pytest
from lib.music_library import *
from lib.track import *

def test_music_library_integration_add_two_tracks_added_to_tracks_list():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)

    result = library.all_tracks
    assert result == [track_1, track_2]

def test_music_library_integration_search_finds_track():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search("Always") == [track_1]

def test_music_library_integration_search_finds_no_tracks():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search("None") == []