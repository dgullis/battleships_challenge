from unittest.mock import Mock

class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.all_tracks = []

    def add(self, track):
        self.all_tracks.append(track)

    def search(self, keyword):
        matched_tracks = []
        for track in self.all_tracks:
            if track.matches(keyword):
                matched_tracks.append(track)
        return matched_tracks