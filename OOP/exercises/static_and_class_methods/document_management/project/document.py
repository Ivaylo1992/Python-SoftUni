from project.category import Category
from project.topic import Topic


class Document:
    def __init__(self, document_id: int, category_id: int, topic_id: int, file_name: str) -> None:
        self.id = document_id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, document_id: int, category: Category, topic: Topic, file_name: str) -> 'Document':
        category_id = category.id
        topic_id = topic.id
        return cls(document_id, category_id, topic_id, file_name)

    def add_tag(self, tag_content: str) -> None:
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str) -> None:
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name: str) -> None:
        self.file_name = file_name

    def __repr__(self) -> str:
        return (f"Document {self.id}: {self.file_name};"
                f" category {self.category_id},"
                f" topic {self.topic_id}, tags:"
                f" {', '.join(self.tags)}")