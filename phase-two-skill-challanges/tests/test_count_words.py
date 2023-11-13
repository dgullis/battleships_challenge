import pytest
from lib.count_words import *

# A function called count_words that takes a string as an argument and returns the number of words in that string.
def test_count_words_zero_words():
    result = count_words("")
    assert result == 0

def test_count_words_five_words():
    result = count_words("one two three four five")
    assert result == 5