from lib.task_list import TaskList
from unittest.mock import Mock

# tests #.tasks behaviour
def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []

# tests #all_complete behaviour
def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# test #add and #all behaviour
def test_tasks_added_all_returns_list():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_2 = Mock()
    fake_task_3 = Mock()
    fake_task_4 = Mock()
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    task_list.add(fake_task_3)
    task_list.add(fake_task_4)
    result = task_list.all()
    assert result == [fake_task_1, fake_task_2, fake_task_3, fake_task_4]

# tests #add and #all_complete behaviour
def test_not_all_tasks_complete():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_2 = Mock()
    fake_task_3 = Mock()
    fake_task_1.is_complete.return_value = False
    fake_task_2.is_complete.return_value = False
    fake_task_3.is_complete.return_value = True
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    task_list.add(fake_task_3)
    result = task_list.all_complete()
    assert result == False

# tests #add and #all_complete behaviour
def test_all_tasks_complete():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_2 = Mock()
    fake_task_3 = Mock()
    fake_task_1.is_complete.return_value = True
    fake_task_2.is_complete.return_value = True
    fake_task_3.is_complete.return_value = True
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    task_list.add(fake_task_3)
    result = task_list.all_complete()
    assert result == True

