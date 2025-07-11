import json
from typing import List, Optional
from .task import Task, Priority, Status

class TaskManager:
    """Gestionnaire principal des tâches"""

    def __init__(self, storage_file="tasks.json"):
        self.tasks = []
        self.storage_file = storage_file

    def add_task(self, title, description="", priority=Priority.MEDIUM):
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task.id

    def get_task(self, task_id) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_tasks_by_status(self, status: Status) -> List[Task]:
        return [task for task in self.tasks if task.status == status]

    def get_tasks_by_priority(self, priority: Priority) -> List[Task]:
        return [task for task in self.tasks if task.priority == priority]

    def delete_task(self, task_id) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def save_to_file(self, filename=None):
        fname = filename or self.storage_file
        try:
            with open(fname, "w") as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        except Exception as e:
            raise IOError(f"Erreur lors de la sauvegarde : {e}")

    def load_from_file(self, filename=None):
        fname = filename or self.storage_file
        try:
            with open(fname, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
        except FileNotFoundError:
            self.tasks = []
        except Exception as e:
            raise IOError(f"Erreur lors du chargement : {e}")

    def get_statistics(self):
        total_tasks = len(self.tasks)
        completed_tasks = len([t for t in self.tasks if t.status == Status.DONE])
        tasks_by_priority = {p.name: 0 for p in Priority}
        tasks_by_status = {s.name: 0 for s in Status}
        for t in self.tasks:
            tasks_by_priority[t.priority.name] += 1
            tasks_by_status[t.status.name] += 1
        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "tasks_by_priority": tasks_by_priority,
            "tasks_by_status": tasks_by_status
        } 