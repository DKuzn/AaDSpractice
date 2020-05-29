from Stack_and_Queue.processor import Processor
from Stack_and_Queue.task import TaskGenerator
from Stack_and_Queue.stack import MyStack


generator = TaskGenerator()
processor = Processor()
cash = MyStack()

for i in range(25):
    generator.gen_task()

while generator.get_task() is not None:
    if processor.idle_proc():
        if not generator.none_task():
            processor.add_task(generator.get_task())
        elif not cash.check_empty():
            processor.add_task(cash.pop())
    else:
        if not generator.queue2.check_empty():
            cash.push(generator.queue2.pop())
    print('Tasks\n', generator)
    print('Stack', cash)
    processor.running()
