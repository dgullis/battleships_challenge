# Track List Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TrackList:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Side effects:
        #   Sets the tracks property of the self object to an empty list
        pass # No code here yet

    def addSong(self, song):
        # Parameters:
        #   song: string representing the name of a song
        # Returns:
        #   Nothing
        # Side-effects
        #   Add the song to the tracks property of the self object
        pass # No code here yet

    def displaySongs(self):
        # Returns:
        #   A string of all songs that have been listened to
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a song, add it to the tracks list
"""
songs = TrackList()
songs.add("Michael Jackson - Thriller")
songs.tracks # => ["Michael Jackson - Thriller"]

"""
Given three songs, add them to the tracks list
"""
songs = TrackList()
songs.add("Michael Jackson - Thriller")
songs.add("Michael Jackson - Beat It")
songs.add("Michael Jackson - Billie Jean")
songs.tracks # => ["Michael Jackson - Thriller", "Michael Jackson - Beat It", "Michael Jackson - Billie Jean"]

"""
Given three songs, return a list of them
"""
songs = TrackList()
songs.add("Michael Jackson - Thriller")
songs.add("Michael Jackson - Beat It")
songs.add("Michael Jackson - Billie Jean")
songs.displaySongs() # => ["Michael Jackson - Thriller", "Michael Jackson - Beat It", "Michael Jackson - Billie Jean"]


"""
Given an empty string to add(), raises an error
"""
songs = TrackList()
songs.add("") # raises an error with the message "No song name provided!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

---