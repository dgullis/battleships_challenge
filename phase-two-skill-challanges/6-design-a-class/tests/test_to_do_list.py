import pytest
from lib.to_do_list import *

def test_add_one_task():
    todos = ToDoList()
    todos.add("Walk the dog")
    result = todos.format()
    assert result == "Walk the dog"

def test_format_three_tasks():
    todos = ToDoList()
    todos.add("Walk the dog")
    todos.add("Wash the dog")
    todos.add("Walk the cat")
    result = todos.format()
    assert result == """Walk the dog
    Wash the dog
    Walk the cat"""

def test_format_complete_task():
    todos = ToDoList()
    todos.add("Walk the dog")
    todos.add("Wash the dog")
    todos.add("Walk the cat")
    todos.complete(2)
    result = todos.format()
    assert result == """Walk the dog
    Walk the cat"""

def test_add_task_to_complete_doesnt_exist():
    todos = ToDoList()
    todos.add("Walk the dog")
    with pytest.raises(Exception) as e:
        todos.complete(-1)
    error_message = str(e.value)
    assert error_message == "No such task to mark complete"