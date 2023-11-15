class TrackList:
    def __init__(self):
        self.tracks = []

    def addSong(self, song):
        if song == "":
            raise Exception("No song name provided!")
        self.tracks.append(song)

    def displaySongs(self):
        return self.tracks