from lib.secret_diary import *
from unittest.mock import Mock

def test_initialisation():
    newDiary = Mock()
    newSecretDiary = SecretDiary(newDiary)
    assert newSecretDiary.diary == newDiary
    assert newSecretDiary.locked == True

def test_read():
    newDiary = Mock()
    newSecretDiary = SecretDiary(newDiary)
    assert newSecretDiary.read() == "Go away!"

def test_unlock():
    newDiary = Mock()
    newSecretDiary = SecretDiary(newDiary)
    newSecretDiary.unlock()
    assert newSecretDiary.locked == False

def test_lock():
    newDiary = Mock()
    newSecretDiary = SecretDiary(newDiary)
    newSecretDiary.unlock()
    newSecretDiary.lock()
    assert newSecretDiary.locked == True


