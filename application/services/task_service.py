from domain.entities.task import Task

class TaskService:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def add_task(self, title):
        """
        Crea una nueva tarea y la guarda en el repositorio.
        """
        new_task = Task(id=None, title=title, completed=False)  # Aquí, None es un marcador de posición para el ID, que se debería generar automáticamente.
        return self.task_repository.add(new_task)

    def get_task(self, task_id):
        """
        Obtiene una tarea por su ID.
        """
        return self.task_repository.get(task_id)

    def get_all_tasks(self):
        """
        Obtiene todas las tareas.
        """
        return self.task_repository.get_all()

    def update_task(self, task_id, title=None, completed=None):
        """
        Actualiza los atributos de una tarea existente.
        """
        task = self.task_repository.get(task_id)
        if task is None:
            return None 
        if title is not None:
            task.title = title
        if completed is not None:
            task.completed = completed

        self.task_repository.update(task)
        return task

    def delete_task(self, task_id):
        """
        Elimina una tarea por su ID.
        """
        return self.task_repository.delete(task_id)
