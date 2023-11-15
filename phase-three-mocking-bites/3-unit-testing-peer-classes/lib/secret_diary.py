class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.locked = True

    def read(self):
        if self.locked == False:
            return self.diary.read()
        return "Go away!"
        
    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False
