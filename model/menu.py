from mongoengine import *

import mlab


class Menu(Document):
    res_id = StringField(max_length=20, min_length=3, required=True)
    menu_id = StringField(max_length=20, min_length=3, unique=True, required=True)
    menu_name = StringField()
    date_create = DateTimeField(required=False)
    describe = StringField(max_length=500)

    def get_json(self):
        return mlab.item2json(self)