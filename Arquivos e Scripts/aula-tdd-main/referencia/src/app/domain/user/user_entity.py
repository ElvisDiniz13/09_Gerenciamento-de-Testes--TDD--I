from uuid import UUID
from domain.task.task_entity import Task
from typing import List


class User:

    id: UUID
    name: str
    tasks: List[Task]

    def __init__(self, id: UUID, name: str):
        self.id = id
        self.name = name
        self.tasks = []
        self.validate()

    def validate(self):
        if not isinstance(self.id, UUID):
            raise Exception("id must be an UUID")

        if not isinstance(self.name, str) or len(self.name) == 0:
            raise Exception("name is required")

    def collect_tasks(self, tasks: List[Task]) -> None:
        self.tasks.extend(tasks)

    def count_pending_tasks(self) -> int:
        count = 0
        for task in self.tasks:
            if task.completed is not True:
                count += 1
        return count
