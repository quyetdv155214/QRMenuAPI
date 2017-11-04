from flask_restful import Resource, reqparse

from model.manager_acc import *


import mlab

class ManagerLogin(Resource):
    #login
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument(name="email", type=str, location='json')
        parser.add_argument(name="password", type=str, location='json')
        body = parser.parse_args()
        email = body["email"]
        password = body["password"]

        manager = Manager.objects()
        for m in manager:
            if m.check_authen(email, password ):
                return {"access_token" : m.get_token}, 200
        return {"message" : "email or password was wrong"},404

class ManagerRegister(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name="email", type=str, location='json')
        parser.add_argument(name="manager_id", type=str, location='json')
        parser.add_argument(name="password", type=str, location='json')
        parser.add_argument(name="manager_name", type=str, location='json')
        parser.add_argument(name="token", type=str, location='json')

        body = parser.parse_args()
        email = body["email"]
        password = body["password"]
        manager_id = body["manager_id"]
