from lib.todo_list import *

def test_constructor():
    new_list = TodoList()
    assert new_list.todos == []