# tests/unit/application/test_task_service.py

from unittest.mock import Mock
from application.services.task_service import TaskService
from domain.entities.task import Task

def test_add_task():
    mock_repo = Mock()
    task_service = TaskService(mock_repo)
    task_service.add_task("New Task")
    mock_repo.add.assert_called_once()  # Verifica que el método add del repositorio fue llamado una vez

def test_get_task():
    mock_repo = Mock()
    mock_repo.get.return_value = Task(id=1, title="Test", completed=False)
    task_service = TaskService(mock_repo)
    
    task = task_service.get_task(1)
    assert task.id == 1
    assert task.title == "Test"
    assert mock_repo.get.called  # Verifica que se llamó al método get del repositorio