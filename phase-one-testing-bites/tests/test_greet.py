from lib.greet import *

def test_greet():
    result = greet("John")
    assert result == "Hello, John!"