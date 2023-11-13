import pytest
from lib.make_snippet import *

# A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.

def test_make_snippet_takes_string():
    result = make_snippet("string")
    assert result == "string"

# def test_make_snippet_rejects_non_strings():
#     with pytest.raises(Exception) as e:
#         make_snippet(500)
#     error_message = str(e.value)
#     assert error_message == "Invalid argument, must be string"


def test_make_snippet_six_words():
    result = make_snippet("Dog Cat House Blue Sun Happy")
    assert result == "Dog Cat House Blue Sun ..."