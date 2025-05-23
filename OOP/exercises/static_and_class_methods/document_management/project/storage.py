from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self) -> None:
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if not self.is_instance_found(self.categories, category):
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if not self.is_instance_found(self.topics, topic):
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if not self.is_instance_found(self.documents, document):
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        self.perform_action(
            "edit", "category", category_id, new_name
        )

    def edit_topic(self, topic_id: int, new_name: str, new_storage_folder) -> None:
        self.perform_action(
            "edit", "topic", topic_id, new_name, new_storage_folder
        )

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self.perform_action(
            "edit", "document", document_id, new_file_name
        )

    def delete_category(self, category_id: int) -> None:
        self.perform_action(
            "delete", "category", category_id
        )

    def delete_topic(self, topic_id: int) -> None:
        self.perform_action(
            "delete", "topic", topic_id
        )

    def delete_document(self, document_id: int) -> None:
        self.perform_action(
            "delete", "document", document_id
        )

    def get_document(self, document_id: int) -> Document | None:
        return next((d for d in self.documents if d.id == document_id), None)

    def __repr__(self):
        result = [d.__repr__() for d in self.documents]
        return "\n".join(result)

    # Helper methods
    def perform_action(
            self,type_of_action: str, instance_type: str, instance_id: int, *args
    ) -> None:
        operations = {
            "edit category": lambda category: category.edit(args[0]),
            "edit topic": lambda topic: topic.edit(args[0], args[1]),
            "edit document": lambda document: document.edit(args[0]),
            "delete category": lambda category: self.categories.remove(category),
            "delete topic": lambda topic: self.topics.remove(topic),
            "delete document": lambda document: self.documents.remove(document),
        }

        collections_mapper = {
            "category": self.categories,
            "topic": self.topics,
            "document": self.documents,
        }

        instance = next(
            (inst for inst in collections_mapper[instance_type] if inst.id == instance_id),
            None
        )

        operation = f"{type_of_action} {instance_type}"

        # Perform the given operation if the instance of the given class is found in the given list
        if instance:
            operations[operation](instance)

    @staticmethod
    def is_instance_found(array, inst):
        return inst in array





