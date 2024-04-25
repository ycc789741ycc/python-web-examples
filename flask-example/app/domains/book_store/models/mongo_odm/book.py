from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, IntField, FloatField


class Author(EmbeddedDocument):
    name = StringField(required=True)
    age = IntField(required=True)


class Book(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    author = EmbeddedDocumentField(Author)
    price = FloatField(required=True)
