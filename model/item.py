from mongoengine import *


class Item(Document):
    menu_id = StringField()
    cate_id = StringField()
    item_id = StringField()
    item_name = StringField()
    item_price = FloatField()
    item_discount = FloatField()
    item_desc = StringField()