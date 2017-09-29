from mongoengine import *


class Restaurant(Document):
    restaurant_id = StringField()
    restaurant_name = StringField()
    restaurant_menus = ListField()

