from lib.task_formatter import *
from unittest.mock import Mock

def test_initialisation():
    newTask = Mock()
    formatter = TaskFormatter(newTask)
    assert formatter.task == newTask

def test_format_task_not_complete():
    newTask = Mock()
    newTask.title = "Incomplete Task"
    newTask.complete = False
    formatter = TaskFormatter(newTask)
    assert formatter.format() == "[ ] Incomplete Task"

def test_format_task_complete():
    newTask = Mock()
    newTask.title = "Complete Task"
    newTask.complete = True
    formatter = TaskFormatter(newTask)
    assert formatter.format() == "[x] Complete Task"