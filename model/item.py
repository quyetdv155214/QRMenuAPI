from mongoengine import *

import mlab


class Item(Document):
    menu_id = StringField()
    cate_id = StringField(required=True)
    item_id = StringField(unique=True, required=True)
    item_name = StringField()
    item_price = FloatField(min_value=0, default=0)
    item_discount = FloatField(min_value=0, max_value=100, default=0)
    item_desc = StringField()
    item_images_url = ListField()

    def get_json(self):
        return mlab.item2json(self)

