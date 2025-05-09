from OOP.exercises.objects_and_classes.to_do_list.project.task import Task


class Section:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, tsk: Task) -> str:
        for t in self.tasks:
            if t.name == tsk.name:
                return f"Task is already in the section {self.name}"

        self.tasks.append(tsk)
        return f"Task {tsk.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        for tsk in self.tasks:
            if tsk.name == task_name:
                setattr(tsk, 'completed', True)
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        cleared_tasks = 0
        for t in self.tasks:
            if t.completed:
                cleared_tasks += 1
                self.tasks.remove(t)

        return f"Cleared {cleared_tasks} tasks."

    def view_section(self) -> str:
        result = f"Section {self.name}:\n"
        for t in self.tasks:
            result += f"{t.details()}\n"

        return result

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())