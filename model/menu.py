from mongoengine import *


class Menu(Document):
    #
    res_id = StringField(max_length=20, min_length=10, unique=True, required=True)
    #
    menu_id = StringField(max_length=20, min_length=10, unique=True, required=True)
    # max_length=100, min_length=1, required=True, unique_with=res_id
    menu_name = StringField()
    date_create = DateTimeField(required=False)
    describe = StringField(max_length=500)
