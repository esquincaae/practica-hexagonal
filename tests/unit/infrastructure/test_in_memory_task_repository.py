# tests/unit/infrastructure/test_in_memory_task_repository.py

from infrastructure.repositories.in_memory_task_repository import InMemoryTaskRepository
from domain.entities.task import Task

def test_add_and_get_task():
    repo = InMemoryTaskRepository()
    task = Task(id=None, title="Test Task", completed=False)
    added_task = repo.add(task)
    
    assert added_task.id is not None
    assert repo.get(added_task.id) == added_task

def test_delete_task():
    repo = InMemoryTaskRepository()
    task = Task(id=None, title="Task to Delete", completed=False)
    added_task = repo.add(task)
    assert repo.delete(added_task.id) is True
    assert repo.get(added_task.id) is None
