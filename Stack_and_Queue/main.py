from Stack_and_Queue.processor import Processor
from Stack_and_Queue.task import TaskGenerator


generator = TaskGenerator()
processor = Processor()

for i in range(50):
    generator.gen_task()

while generator.get_task() is not None:
    task = generator.get_task()
    if processor.idle_proc():
        if not generator.none_task():
            processor.add_task(task)
        elif not processor.wait.check_empty():
            processor.add_task(processor.wait.pop())
    print('Tasks\n', generator)
    print('Stack:', processor.wait)
    processor.running()
