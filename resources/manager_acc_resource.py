from flask_restful import Resource, reqparse

from model.manager_acc import *

import mlab


class ManagerLogin(Resource):
    # login
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument(name="email", type=str, location='json')
        parser.add_argument(name="password", type=str, location='json')
        body = parser.parse_args()
        email = body["email"]
        password = body["password"]
        #
        manager = Manager.objects()
        for m in manager:
            if m.email == email and m.password == password:
                return {"manager_id": m.manager_id}, 200
        return {"message": "email or password was wrong"}, 404


class ManagerRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name="email", type=str, location='json')
        parser.add_argument(name="manager_id", type=str, location='json')
        parser.add_argument(name="password", type=str, location='json')
        parser.add_argument(name="manager_name", type=str, location='json')
        # parser.add_argument(name="token", type=str, location='json')

        body = parser.parse_args()
        email = body["email"]
        password = body["password"]
        manager_id = body["manager_id"]
        manager_name = body["manager_id"]
        cr_managers = Manager.objects()

        for m in cr_managers:
            if m.email == email:
                return {"message": "Email has exit"}, 400

        manager = Manager(email=email, password=password, manager_id=manager_id, manager_name=manager_name)
        manager.save()

        return manager.get_json(), 200
