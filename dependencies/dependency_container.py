from infrastructure.repositories.in_memory_task_repository import InMemoryTaskRepository
from application.services.task_service import TaskService

task_repository = InMemoryTaskRepository()
task_service = TaskService(task_repository)
