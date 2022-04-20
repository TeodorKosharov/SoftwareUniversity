from Exercise.Document_Management.project.category import Category
from Exercise.Document_Management.project.document import Document
from Exercise.Document_Management.project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        [category for category in self.categories if category.id == category_id][0].name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        [document for document in self.documents if document.id == document_id][0].file_name = new_file_name

    def delete_category(self, category_id: int):
        self.categories.remove([category for category in self.categories if category.id == category_id][0])

    def delete_topic(self, topic_id):
        self.topics.remove([topic for topic in self.topics if topic.id == topic_id][0])

    def delete_document(self, document_id):
        self.documents.remove([document for document in self.documents if document.id == document_id][0])

    def get_document(self, document_id):
        return [document for document in self.documents if document.id == document_id][0]

    def __repr__(self):
        return '\n'.join([str(x) for x in self.documents])
