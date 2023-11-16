from lib.todo_list import *
from lib.todo import *

def test_todo_list_two_tasks_incomplete():
    new_list = TodoList()
    task_one = Todo("Wash the car")
    task_two = Todo("Wash the dog")

    new_list.add(task_one)
    new_list.add(task_two)
    assert new_list.incomplete() == [task_one, task_two]
    assert new_list.complete() == []

def test_todo_list_give_up_with_two_tasks():
    new_list = TodoList()
    task_one = Todo("Wash the car")
    task_two = Todo("Wash the dog")

    new_list.add(task_one)
    new_list.add(task_two)
    new_list.give_up()
    assert new_list.incomplete() == []
    assert new_list.complete() == [task_one, task_two]

def test_todo_list_mark_complete_one__of_three_tasks():
    new_list = TodoList()
    task_one = Todo("Wash the car")
    task_two = Todo("Wash the dog")
    task_three = Todo("Wash the house")

    new_list.add(task_one)
    new_list.add(task_two)
    new_list.add(task_three)

    task_two.mark_complete()
    
    assert new_list.incomplete() == [task_one, task_three]
    assert new_list.complete() == [task_two]