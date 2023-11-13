import pytest
from lib.includes_todo import *

def test_includes_todo_false():
    result = includes_todo("hello world")
    assert result == False

def test_includes_todo_true():
    result = includes_todo("#TODO Brush Teeth")
    assert result == True

def test_includes_todo_empty():
    result = includes_todo("")
    assert result == False

def test_includes_todo_lowercase():
    result = includes_todo("#todo Tidy Up")
    assert result == True

def test_includes_todo_middle():
    result = includes_todo("Tidy #TODO Up")
    assert result == True

def test_includes_todo_end():
    result = includes_todo("Tidy up #TODO")
    assert result == True

def test_includes_todo_non_string():
    with pytest.raises(Exception) as e:
        includes_todo(5)
    error_message = str(e.value)
    assert error_message == "Function only accepts strings!"