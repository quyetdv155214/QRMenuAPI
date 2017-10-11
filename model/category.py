from mongoengine import *

import mlab
from model import *


class Categoty(Document):
    menu_id = StringField(max_length=20, min_length=3, required=True)
    cate_id = StringField(max_length=20, min_length=3, unique=True, required=True)
    cate_name = StringField(max_length=200, min_length=1, required=True)
    cate_type = StringField()
    cate_order = IntField(min_value=1, default=1)

    def get_json(self):
        return mlab.item2json(self)