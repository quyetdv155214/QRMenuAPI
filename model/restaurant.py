from mongoengine import *

import mlab


class Restaurant(Document):
    manager_id =StringField(required=True)
    res_id = StringField(max_length=100, min_length=5, unique=True, required=True)
    res_name = StringField(max_length=200, min_length=1, required=True)
    res_type = StringField()
    view_count = IntField(default=0, min_value=0)
    address = StringField()
    phone = StringField()
    describe = StringField(max_length=500)
    def get_json(self):
        return mlab.item2json(self)