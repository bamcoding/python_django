from mongoengine import *
connect('my_database')

# Create your models here.
class Article(Document):
    title = StringField(max_length=50, required=True)
    contents = StringField(max_length=50, required=True)
    lastDate = DateTimeField(required=True)
