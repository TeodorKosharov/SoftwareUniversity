from Exercise.TodoList.project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task.name in [x.name for x in self.tasks]:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for current_task in self.tasks:
            if current_task.name == task_name:
                current_task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        current_tasks = len(self.tasks)
        self.tasks = [x for x in self.tasks if not x.completed]
        return f"Cleared {current_tasks - len(self.tasks)} tasks."

    def view_section(self):
        result = f"Section {self.name}:" + "\n"
        for task_info in self.tasks:
            result += task_info.details() + "\n"
        return result
