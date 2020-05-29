from dataclasses import dataclass
from Stack_and_Queue.queue import MyQueue
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

    def __str__(self):
        return '[' + str(self.get_type()) + ',' + str(self.get_time()) + ']'

    def get_time(self):
        return self.current_task.time

    def get_type(self):
        return self.current_task.type


class TaskGenerator:
    def __init__(self):
        self.queue1 = MyQueue()
        self.queue2 = MyQueue()

    def gen_task(self):
        task = Task()
        if task.get_type() == 1:
            self.queue1.push(task)
        else:
            self.queue2.push(task)

    def get_task(self):
        queue = rd.randint(1, 2)
        if queue == 1:
            task = self.queue1.pop()
        else:
            task = self.queue2.pop()
        return task
