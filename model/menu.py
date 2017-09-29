from mongoengine import *
from model.item import *


class Menu(Document):
    menu_id = StringField()
    menu_name = StringField()
    menu_categories = ListField()
    # menu_items = ListField(ReferenceField(Item))
