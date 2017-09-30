from mongoengine import *


class RestauranInfo(EmbeddedDocument):
    address = StringField()
    phone = StringField()
    describe = StringField(max_length=500)