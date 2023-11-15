from lib.secret_diary import *
from lib.diary import *

def test_secret_diary_integration_initialise_locked():
    newDiary = Diary("")
    newSecretDiary = SecretDiary(newDiary)

    result = newSecretDiary.read()
    assert result == "Go away!"

def test_secret_diary_integration_unlock():
    newDiary = Diary("Contents of Diary")
    newSecretDiary = SecretDiary(newDiary)

    newSecretDiary.unlock()
    result = newSecretDiary.read()
    assert result == "Contents of Diary"

def test_secret_diary_integration_lock():
    newDiary = Diary("Contents of Diary")
    newSecretDiary = SecretDiary(newDiary)

    newSecretDiary.unlock()
    newSecretDiary.lock()
    result = newSecretDiary.read()
    assert result == "Go away!"




