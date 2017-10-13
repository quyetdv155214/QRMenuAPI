from flask_restful import Resource, reqparse
from model.restaurant import *
from model.restaurant_info import *
from flask import Response

from flask import jsonify
import mlab


class RestaurantRes(Resource):

    def get(self):
        restaurants = Restaurant.objects()
        if not restaurants:
            message = {"message": "No restaurant found"}
            resp = jsonify(message)
            resp.status_code = 200
        else:
            resp = jsonify(mlab.list2json(restaurants))
            resp.status_code = 200
        # resp= mlab.list2json(restaurants)

        return resp

    def post(self):
        parser = reqparse.RequestParser()
        parser1 = reqparse.RequestParser()
        #
        # parser1.add_argument(name="address", type=str, location="json")
        # parser1.add_argument(name="phone", type=str, location="json")
        # parser1.add_argument(name="describe", type=str, location="json")
        #
        # body1 = parser1.parse_args()
        # address = body1["address"]
        # phone = body1["phone"]
        # describe = body1["describe"]
        #
        # restau_info = RestauranInfo(address=address, phone=phone, describe=describe)

        parser.add_argument(name="res_id", type=str, location="json")
        parser.add_argument(name="res_name", type=str, location="json")
        parser.add_argument(name="res_type", type=str, location="json", action='append')
        # parser.add_argument(name="describe", type=RestauranInfo, location="json")
        parser.add_argument(name="view_count", type=int, location="json")

        body = parser.parse_args()

        res_id = body["res_id"]
        res_name = body["res_name"]
        res_type = body["res_type"]
        # describe = restau_info
        view_count = body["view_count"]

        restaurant = Restaurant(res_id=res_id, res_name=res_name, res_type=res_type, view_count=view_count)

        restaurant.save()

        added_menu = Restaurant.objects().with_id(restaurant.id)
        return mlab.item2json(added_menu)
        #
        # "describe": {
        #     "address": "o dau do",
        #     "phone": "3029302",
        #     "describe": "aasdfasdfsdf"
        # },