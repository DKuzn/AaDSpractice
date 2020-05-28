from dataclasses import dataclass
import random as rd


@dataclass()
class TaskData:
    time: int = None
    type: int = None


class Task:
    def __init__(self):
        self.current_task = TaskData()
        self.current_task.time = rd.randint(1, 4)
        self.current_task.type = rd.randint(1, 2)

    def get_time(self):
        return self.current_task.time

    def get_type(self):
        return self.current_task.type
