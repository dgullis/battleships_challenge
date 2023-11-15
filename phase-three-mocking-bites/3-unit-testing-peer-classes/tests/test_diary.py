from lib.diary import *
import pytest


def test_initialisation():
    newDiary = Diary("contents of diary")
    result = newDiary.contents
    assert result == "contents of diary"

def test_read():
    newDiary = Diary("contents of diary")
    result = newDiary.read()
    assert result == "contents of diary"

def test_read_empty_contents():
    newDiary = Diary("")
    result = newDiary.read()
    assert result == ""

def test_contents_not_string_raise_error():
    with pytest.raises(TypeError) as e:
        newDiary = Diary(5)
    assert str(e.value) == "Contents not string!"