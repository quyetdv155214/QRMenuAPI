from mongoengine import *

import mlab
from model.menu import Menu


class User(Document):
    id_user = StringField()
    name = StringField()
    address = StringField()
    phone_number = StringField()
    email = StringField()
    password = StringField()
    urlPic = StringField()
    token = StringField()
    save_menus = ListField(ReferenceField(Menu))

    def get_json(self):
        return {
            "id_user": self.id_user,
            "name": self.id_user,
            "address": self.id_user,
            "phone_number": self.id_user,
            "email": self.id_user,
            "password": self.id_user,
            "urlPic": self.urlPic,
            "token": self.token,
        }

    def get_token(self):
        return {
            "token": self.token
        }

    def check_authen(self, email, password):
        if self.email == email and self.password == password:
            return True
        else:
            return False
