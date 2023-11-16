import pytest
from lib.todo import *

# Test constructor
def test_constructor():
    task = Todo("Wash the car")
    assert task.task == "Wash the car"
    assert task.complete == False

# Test mark_complete()
def test_mark_complete():
    task = Todo("Wash the car")
    task.mark_complete()
    assert task.complete == True


# Test non string being passed as argument to constructor
def test_constructor_non_string_passed():
    with pytest.raises(Exception) as e:
        task = Todo(5)
    result = str(e.value)
    assert result == "Todo class only accepts strings as argument!"