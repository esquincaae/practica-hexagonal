# tests/unit/domain/test_task.py

from domain.entities.task import Task

def test_task_creation():
    task = Task(id=1, title="Test Task", completed=False)
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.completed is False
