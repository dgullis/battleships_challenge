class Diary:
    def __init__(self, contents):
        if type(contents) is not str:
            raise TypeError("Contents not string!")
        self.contents = contents

    def read(self):
        return self.contents