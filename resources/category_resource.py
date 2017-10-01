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

    def post(self):
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
        added_cate = Categoty.objects().with_id(cate.id)
        return mlab.item2json(cate)
    def delete(self):
        cates = Categoty.objects()
        for cate in cates:
            cate.delete()
        return {"message": "delete all category"}
