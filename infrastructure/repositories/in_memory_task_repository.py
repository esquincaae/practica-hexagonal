class InMemoryTaskRepository:
    def __init__(self):
        self.tasks = {}
        self._next_id = 1

    def add(self, task):
        task.id = self._next_id
        self.tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get(self, task_id):
        return self.tasks.get(task_id)

    def get_all(self):
        return list(self.tasks.values())

    def update(self, task):
        if task.id in self.tasks:
            self.tasks[task.id] = task
            return task
        return None

    def delete(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
