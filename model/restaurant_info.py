from mongoengine import *

import mlab


class RestauranInfo(EmbeddedDocument):
    address = StringField()
    phone = StringField()
    describe = StringField(max_length=500)

    def get_json(self):
        return mlab.item2json(self)