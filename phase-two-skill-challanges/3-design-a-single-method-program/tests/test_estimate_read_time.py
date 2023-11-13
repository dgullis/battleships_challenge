import pytest
from lib.estimate_read_time import *

def test_estimate_read_time_empty():
    assert estimate_read_time("") == "00:00:00"

def test_estimate_read_time_20_words():
    assert estimate_read_time("one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty") == "00:00:06"

def test_estimate_read_time_200_words():
    assert estimate_read_time("word "*200) == "00:01:00"

def test_estimate_read_time_288000_words():
    assert estimate_read_time("word "*278000) == "23:10:00"