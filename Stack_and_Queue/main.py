from Stack_and_Queue.processor import Processor
from Stack_and_Queue.task import TaskGenerator
from Stack_and_Queue.stack import MyStack


generator = TaskGenerator()
processor = Processor()
cash = MyStack()

for i in range(50):
    generator.gen_task()

while generator.get_task() is not None:
    task = generator.get_task()
    if processor.idle_proc():
        if not generator.none_task():
            processor.add_task(task)
        elif not cash.check_empty():
            processor.add_task(cash.pop())
    else:
        cash.push(task)
    print('Stack before:', cash)
    print('Tasks\n', generator)
    print('Stack after:', cash)
    processor.running()
