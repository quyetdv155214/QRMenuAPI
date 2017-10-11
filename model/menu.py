from mongoengine import *

import mlab
from model.category import Categoty
from model.item import Item


class Menu(Document):
    res_id = StringField(max_length=20, min_length=3, required=True)
    menu_id = StringField(max_length=20, min_length=3, unique=True, required=True)
    menu_name = StringField()
    date_create = StringField(required=False)
    describe = StringField(max_length=500)
    # list category
    categories = ListField(ReferenceField(Categoty))
    # list item
    items = ListField(ReferenceField(Item))

    def get_json(self):
        str = mlab.item2json(self)
        oid = str["_id"]["$oid"]
        return {
            "id_data": oid,
            "res_id": self.res_id,
            "menu_id": self.menu_id,
            "menu_name": self.menu_name,
            "date_create": self.date_create,
            "describe": self.describe,
            "categories": [cate.get_json() for cate in self.categories],
            "items": [item.get_json() for item in self.items]
        }