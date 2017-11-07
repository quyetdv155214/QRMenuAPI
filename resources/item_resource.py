import random

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
        # parser.add_argument(name="item_discount", type=float, location='json')
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
        listImage = ["http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201423/bigstar_6281.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201422/tom-b_8200.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201635/1a_7975.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201422/chicken-ball-rice_1604.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201424/soup_7846.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201635/4a_858.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201422/pho-mai-que_5719.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201422/gavien_6350.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201710/hash-brown-n_9432.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201422/hot-pie-_7269.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201422/kem-ly-b_4978.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201422/kem-cay_4637.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201422/corn-salad---2_8590.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201422/soy-bean-chicken-rice_2175.png&zc=1",
                     "http://www.lotteria.vn/resize.php?w=250&h=250&src=data/201640/lotteria---ga-sot---set_5668.png&zc=1"]
        item_images_url.append(listImage[random.randint(0, 14)])
        item_images_url.append(listImage[random.randint(0, 14)])
        item_images_url.append(listImage[random.randint(0, 14)])
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
                    item_desc=item_desc, item_info=item_info, item_old_price=0,
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
                    set__item_old_price=item_old_price, set__item_info=item_info,
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
    def get(self, item_id):
        try:
            item = Item.objects(item_id=item_id).first()
        except Exception:
            return {"message": "Item id not exit"}, 400
        if item is None:
            return {"message": "Item id not exit"}, 400

        new_view = item.item_view_count + 1

        item.update(set__item_view_count=new_view)
        return {"view_count": new_view}, 200


class ItemWithMenuId(Resource):
    def get(self, menu_id):
        items = Item.objects(menu_id=menu_id)
        return mlab.list2json(items)


class GetItemWithCateID(Resource):
    def get(self, cate_id):
        item = Item.objects(cate_id=cate_id)

        return mlab.list2json(item)
