from flask_restful import Resource, reqparse
from model.menu import Menu
from model.item import Item
from model.category import Categoty
import mlab
from datetime import datetime


class CategoryRes(Resource):
    def get(self):
        cate = Categoty.objects()
        return mlab.list2json(cate)

    def post(self):  # add a category
        parser = reqparse.RequestParser()

        parser.add_argument(name="menu_id", type=str, location='json')
        parser.add_argument(name="cate_id", type=str, location='json')
        parser.add_argument(name="cate_name", type=str, location='json')
        parser.add_argument(name="cate_type", type=str, location='json')
        parser.add_argument(name="cate_order", type=int, location='json')

        body = parser.parse_args()

        menu_id = body["menu_id"]
        cate_id = body["cate_id"]
        cate_name = body["cate_name"]
        cate_type = body["cate_type"]
        cate_order = body["cate_order"]

        cate = Categoty(menu_id=menu_id, cate_id=cate_id,
                        cate_name=cate_name, cate_type=cate_type, cate_order=cate_order)
        cate.save()
        # added_cate = Categoty.objects().with_id(cate.id)

        return {"message": "add success"}, 200

    # delete all category
    def delete(self):
        cates = Categoty.objects()
        for cate in cates:
            cate.delete()
        return {"message": "delete all category"}, 200


class CateoryWithID(Resource):
    # get category with cate_id
    def get(self, cate_id):
        try:
            category = Categoty.objects().with_id(cate_id)
        except Exception:
            return {'message':"this id is wrong"}, 404

        return mlab.item2json(category)

    def put(self, cate_id):
        try:
            category = Categoty.objects().with_id(cate_id)
        except Exception:
            return {'message':"this id is wrong"}, 404

        parser = reqparse.RequestParser()
        parser.add_argument(name="menu_id", type=str, location='json')
        # parser.add_argument(name="cate_id", type=str, location='json')
        parser.add_argument(name="cate_name", type=str, location='json')
        parser.add_argument(name="cate_type", type=str, location='json')
        parser.add_argument(name="cate_order", type=int, location='json')

        body = parser.parse_args()

        menu_id = body["menu_id"]
        # cate_id = body["cate_id"]
        cate_name = body["cate_name"]
        cate_type = body["cate_type"]
        cate_order = body["cate_order"]

        category.update(set__menu_id=menu_id,
                        set__cate_name=cate_name, set__cate_type=cate_type, set__cate_order=cate_order)
        return mlab.item2json(Categoty.objects().with_id(category.id))



