from flask_restful import Resource, reqparse
from model.restaurant import *
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

        parser.add_argument(name="res_id", type=str, location="json")
        parser.add_argument(name="manager_id", type=str, location="json")
        parser.add_argument(name="res_name", type=str, location="json")
        parser.add_argument(name="res_type", type=str, location="json")
        parser.add_argument(name="address", type=str, location="json")
        parser.add_argument(name="phone", type=str, location="json")
        parser.add_argument(name="describe", type=str, location="json")

        body = parser.parse_args()

        res_id = body["res_id"]
        manager_id = body["manager_id"]
        res_name = body["res_name"]
        res_type = body["res_type"]
        address = body["address"]
        phone = body["phone"]
        describe = body["describe"]

        restaurant = Restaurant(res_id=res_id, manager_id=manager_id, res_name=res_name, res_type=res_type,
                                address=address, phone=phone, describe=describe)

        restaurant.save()

        added_menu = Restaurant.objects().with_id(restaurant.id)
        return mlab.item2json(added_menu)


class EditRestaurant(Resource):
    def put(self, res_id):
        restaurant = Restaurant.objects(res_id=res_id).first()
        parser = reqparse.RequestParser()

        # parser.add_argument(name="res_id", type=str, location="json")
        parser.add_argument(name="res_name", type=str, location="json")
        parser.add_argument(name="res_type", type=str, location="json")
        parser.add_argument(name="address", type=str, location="json")
        parser.add_argument(name="phone", type=str, location="json")
        parser.add_argument(name="describe", type=str, location="json")

        body = parser.parse_args()
        # res_id = body["res_id"]
        res_name = body["res_name"]
        res_type = body["res_type"]
        address = body["address"]
        phone = body["phone"]
        describe = body["describe"]

        restaurant.update(set__res_name=res_name, set__res_type=res_type,
                          set__address=address, set__phone=phone, set__describe=describe)

        edited_res = Restaurant.objects().with_id(restaurant.id)
        return edited_res, 200
