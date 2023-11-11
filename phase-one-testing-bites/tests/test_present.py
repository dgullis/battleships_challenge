import pytest
from lib.present import *

def test_present_wrap():
    present = Present()
    present.wrap("Car")
    result = present.unwrap()
    assert result == "Car"

def test_present_none_unwrap():
    present = Present()
    with pytest.raises(Exception) as e:
        result = present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_present_wrap_twice():
    present = Present()
    present.wrap("Dog")
    with pytest.raises(Exception) as e:
        present.wrap("Car")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."