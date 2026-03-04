class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed!")


class User:
    def __init__(self, name):
        self.name = name
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.title] = task
        print(f"Task '{task.title}' added for {self.name}")

    def complete_task(self, title):
        if title in self.tasks:
            self.tasks[title].complete()
        else:
            print("Task not found.")