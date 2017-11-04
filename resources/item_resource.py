from flask_restful import Resource, reqparse
from model.menu import Menu
from model.item import Item
from datetime import datetime
from util.resp_handle import *

import mlab


class ItemRes(Resource):
    def get(self):
        # get all item
        items = Item.objects()

        return mlab.list2json(items), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name="menu_id", type=str, location='json')
        parser.add_argument(name="cate_id", type=str, location='json')
        parser.add_argument(name="item_id", type=str, location='json')
        parser.add_argument(name="item_name", type=str, location='json')
        parser.add_argument(name="item_price", type=float, location='json')
        # parser.add_argument(name="item_discount", type=float, location='json')
        parser.add_argument(name="item_discount", type=float, location='json')
        parser.add_argument(name="item_desc", type=str, location='json')
        parser.add_argument(name="item_images_url", type=str, location='json', action='append')
        parser.add_argument(name="item_info", type=str, location='json')

        body = parser.parse_args()

        menu_id = body["menu_id"]
        cate_id = body["cate_id"]
        item_id = body["item_id"]
        item_name = body["item_name"]
        item_price = body["item_price"]
        # item_discount = body["item_discount"]
        item_desc = body["item_desc"]
        item_images_url = body["item_images_url"]
        item_info = body["item_info"]

        cur_items = Item.objects()

        for c in cur_items:
            if item_id is None:
                return {"message": "Item id required"}, 400
            if cate_id is None:
                return {"message": "Cate id required"}, 400
            if item_price < 0:
                return {"message": "Price must be > 0"}, 400

            if c["item_id"] == item_id:
                return {"message": "Item id exited"}, 400

        item = Item(menu_id=menu_id, cate_id=cate_id, item_id=item_id, item_name=item_name, item_price=item_price,
                    item_desc=item_desc, item_info=item_info,
                    item_images_url=item_images_url)
        item.save()

        # added_item = Item.objects().with_id(item.id)

        return {"message": "add success"}, 200


class ItemWithID(Resource):
    def get(self, item_id):
        try:
            item = Item.objects(item_id=item_id).first()
        except Exception:
            return {"message": "Item id not exit"}, 400
        if item is None:
            return {"message": "Item id not exit"}, 400
        return item.get_json()

    def put(self, item_id):
        try:
            item = Item.objects(item_id=item_id).first()
        except Exception:
            return {"message": "Item id not exit"}, 400
        if item is None:
            return {"message": "Item id not exit"}, 400
        parser = reqparse.RequestParser()

        parser.add_argument(name="menu_id", type=str, location='json')
        parser.add_argument(name="cate_id", type=str, location='json')
        parser.add_argument(name="item_id", type=str, location='json')
        parser.add_argument(name="item_name", type=str, location='json')
        parser.add_argument(name="item_price", type=float, location='json')
        # parser.add_argument(name="item_discount", type=float, location='json')
        parser.add_argument(name="item_discount", type=float, location='json')
        parser.add_argument(name="item_desc", type=str, location='json')
        parser.add_argument(name="item_info", type=str, location='json')
        parser.add_argument(name="item_images_url", type=str, location='json', action='append')

        body = parser.parse_args()
        item_old_price = item.item_price
        menu_id = body["menu_id"]
        cate_id = body["cate_id"]
        # item_id = body["item_id"]
        item_name = body["item_name"]
        item_price = body["item_price"]
        # item_discount = body["item_discount"]
        item_desc = body["item_desc"]
        item_info = body["item_info"]
        item_images_url = body["item_images_url"]

        item.update(set__menu_id=menu_id, set__cate_id=cate_id, set__item_name=item_name, set__item_price=item_price,
                    set_item_old_price=item_old_price, item_info=item_info,
                    set__item_desc=item_desc, set__item_images_url=item_images_url)

        added_item = Item.objects().with_id(item.id)

        return mlab.item2json(added_item)

    def delete(self, item_id):
        try:
            item = Item.objects(item_id=item_id).first()
        except Exception:
            return {"message": "Item id not exit"}, 400
        if item is None:
            return {"message": "Item id not exit"}, 400
        item.delete()

        return {"message": "deleted item"}


class ViewCount(Resource):
    def put(self, item_id):
        try:
            item = Item.objects(item_id=item_id).first()
        except Exception:
            return {"message": "Item id not exit"}, 400

        if item is None:
            return {"message": "Item id not exit"}, 400

        parser = reqparse.RequestParser()
        parser.add_argument(name="value", type=int, location='json')

        body = parser.parse_args()

        value = body["value"]

        new_view = item.item_view_count + value

        item.update(set__item_view_count=new_view)
        return {"message": "update view count"}, 200


class ItemWithMenuId(Resource):
    def get(self, menu_id):
        items = Item.objects(menu_id=menu_id)
        return mlab.list2json(items)
