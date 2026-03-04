class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True
        print("\u2705 Task '" + self.title + "' completed.")

    def __str__(self):
        status = "\u2705" if self.completed else "\u274c"
        return status + " " + self.title + (" - " + self.description if self.description else "")


class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("\U0001f4cc Task '" + task.title + "' added to " + self.name + ".")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.complete()
                return
        print("Task '" + title + "' not found for user '" + self.name + "'.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found for user '" + self.name + "'.")
        else:
            print("Tasks for " + self.name + ":")
            for task in self.tasks:
                print("  " + str(task))

    def __str__(self):
        return "User: " + self.name + " (" + str(len(self.tasks)) + " task(s))"