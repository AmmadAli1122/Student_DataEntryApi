from mongoengine import Document, StringField, DateTimeField, IntField
from datetime import datetime

class Book(Document):
    Name = StringField(required=True, max_length=100)
    F_Name = StringField(required=True, max_length=100)
    Gender = StringField(required=True, max_length=100)
    Class = IntField(required=True)
    Age = IntField(required=True)
    Date = DateTimeField(default=datetime.utcnow)  

    def __str__(self):
        return self.Name

    meta = {
        'collection': 'data'
    }
