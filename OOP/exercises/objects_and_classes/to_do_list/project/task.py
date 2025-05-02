class Task:
    def __init__(self, name: str, due_date: str) -> None:
        self.name = name
        self.due_date = due_date
        self.comments: list = []
        self.completed: bool = False

    def change_name(self, new_name: str) -> str:
        message = new_name if new_name != self.name else "Name cannot be the same."
        self.name = new_name
        return message

    def change_due_date(self, new_date: str) -> str:
        message = new_date if new_date != self.due_date else "Date cannot be the same."
        self.due_date = new_date
        return message

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        if 0 < comment_number > len(self.comments) - 1:
            return "Cannot find comment."

        self.comments[comment_number] = new_comment
        return ', '.join(self.comments)

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"

