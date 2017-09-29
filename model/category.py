from mongoengine import *
from model import *

class Categoty:
    # menu_id = StringField()
    cate_id = StringField()
    cate_name = StringField()
    cate_type = IntField()
