from mongoengine import *
from model.restaurant_info import *

class Restaurant(Document):
    res_id = StringField(max_length=20, min_length=10, unique=True, required=True)
    res_name = StringField(max_length=200, min_length=1, required=True)
    res_type = ListField(field=StringField)
    # describe = EmbeddedDocumentListField(RestauranInfo)
    view_count = IntField(default=0, min_value=0)
