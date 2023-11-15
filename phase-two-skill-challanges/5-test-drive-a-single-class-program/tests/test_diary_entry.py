import pytest
from lib.diary_entry import *

def test_format():
    entry = DiaryEntry('Title', 'These are the contents')
    result = entry.format()
    assert result == 'Title : These are the contents'

def test_count_words():
    entry = DiaryEntry('Title', 'These are the contents')
    result = entry.count_words()
    assert result == 4


def test_reading_time():
    entry = DiaryEntry('Title', 'These are the contents')
    result = entry.reading_time(4)
    assert result == 1

def test_reading_chunk_all():
    entry = DiaryEntry('Title', 'These are the contents')
    result = entry.reading_chunk(4, 1)
    assert result == 'These are the contents'

def test_reading_chunk_half():
    entry = DiaryEntry('Title', 'These are the contents')
    result = entry.reading_chunk(2, 1)
    assert result == 'These are'

def test_reading_chunk_three_times():
    entry = DiaryEntry('Title', 'These are the contents')
    entry.reading_chunk(2, 1)
    entry.reading_chunk(1, 1)
    result = entry.reading_chunk(1, 1)
    assert result == 'contents'

def test_reading_chunk_restart():
    entry = DiaryEntry('Title', 'These are the contents')
    entry.reading_chunk(2, 1)
    entry.reading_chunk(1, 1)
    entry.reading_chunk(1, 1)
    result = entry.reading_chunk(2, 1)
    assert result == 'These are'