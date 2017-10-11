from mongoengine import *

import mlab
from model import *
from model.item import Item


class Categoty(Document):
    menu_id = StringField(max_length=20, min_length=3, required=True)
    cate_id = StringField(max_length=20, min_length=3, unique=True, required=True)
    cate_name = StringField(max_length=200, min_length=1, required=True)
    cate_type = StringField()
    cate_order = IntField(min_value=1, default=1)
    items =ListField(ReferenceField(Item))

    def get_json(self):
        str = mlab.item2json(self)
        oid = str["_id"]["$oid"]
        return {
            "id_data": oid,
            "menu_id": self.menu_id,
            "cate_id": self.cate_id,
            "cate_name": self.cate_name,
            "cate_type": self.cate_type,
            "cate_order": self.cate_order,
            "items": [item.get_json() for item in self.items]
        }