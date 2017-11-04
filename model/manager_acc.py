from mongoengine import *

import mlab

class manager:
    manager_id = StringField()
    manager_name = StringField()
    email = StringField()
    password = StringField()
    token = StringField()
    def get_json(self):
        return {
            "manager_id": self.manager_id,
            "manager_name": self.manager_name,
            "email": self.email,
            "password": self.password,
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
