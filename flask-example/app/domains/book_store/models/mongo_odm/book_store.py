from mongoengine import Document, StringField


class BookStore(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    location = StringField(required=True)