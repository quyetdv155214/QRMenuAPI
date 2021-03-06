from flask_restful import Resource, reqparse
from model.menu import *
from model.item import Item
from model.category import *
from util.resp_handle import *
from flask import jsonify

import mlab


class MenuWithID(Resource):
    def get(self, menu_id):
        try:
            menu = Menu.objects(menu_id=menu_id).first()
            categories = Categoty.objects(menu_id=menu_id)
            # items = Item.objects(menu_id=menu_id)
            items = Item.objects(menu_id=menu_id)

            # temp_cates =[]

            for cate in categories:
                for item in items:
                    if item.cate_id == cate.cate_id:
                        cate.items.append(item)

            menu.categories = categories

            # menu.items = items

        except Exception:
            mess = {"message": "menu id not exit"}
            return RespHandle.get_resp(mess=mess, code=204)
        return menu.get_json()

    def put(self, menu_id):
        menu = Menu.objects(menu_id=menu_id).first()
        parser = reqparse.RequestParser()

        parser.add_argument(name="menu_name", type=str, location="json")
        parser.add_argument(name="describe", type=str, location="json")
        parser.add_argument(name="menu_pic", type=str, location="json")
        # parse body
        body = parser.parse_args()

        menu_name = body["menu_name"]
        # date_create = menu["date_create"]
        describe = body["describe"]
        menu_pic = body["menu_pic"]

        menu.update(set__menu_pic=menu_pic, set__menu_name=menu_name, set__describe=describe)

        edited_menu = Menu.objects().with_id(menu.id)

        return edited_menu, 200

    def delete(self, menu_id):
        try:
            menu = Menu.objects(menu_id=menu_id).first()
        except Exception:
            mess = {"message": "menu id not exit"}
            return RespHandle.get_resp(mess=mess, code=204)
        if menu is None:
            mess = {"message": "menu not found!"}
            return RespHandle.get_resp(mess=mess, code=204)
        else:
            menu.delete()
            mess = {"message": "delete success"}
            return RespHandle.get_resp(mess=mess, code=200)


class Menus(Resource):
    # get all menu
    def get(self):
        menu = Menu.objects()
        if menu is None:
            return {"message": "menu is null"}
        menu_json = mlab.list2json(menu)
        return menu_json

    # add menu
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name="manager_id", type=str, location="json")
        parser.add_argument(name="menu_id", type=str, location="json")
        parser.add_argument(name="menu_name", type=str, location="json")
        parser.add_argument(name="date_create", type=str, location="json")
        parser.add_argument(name="describe", type=str, location="json")
        parser.add_argument(name="menu_pic", type=str, location="json")
        parser.add_argument(name="categories", type=list, location="json")
        parser.add_argument(name="items", type=list, location="json")

        # parse body
        body = parser.parse_args()
        # getdata from body
        manager_id = body["manager_id"]
        menu_id = body["menu_id"]
        menu_name = body["menu_name"]
        date_create = body["date_create"]
        describe = body["describe"]
        menu_pic = body["menu_pic"]
        categories = body["categories"]
        items = body["items"]

        curent_menus = Menu.objects()
        # check require field
        if manager_id is None:
            mess = {"message": "Restaurant id is required"}
            return RespHandle.get_resp(mess=mess, code=400)
        if menu_id is None:
            mess = {"message": "Menu id is required"}
            return RespHandle.get_resp(mess=mess, code=400)

        # check exit id
        for m in curent_menus:

            c_menu_id = m["menu_id"]

            if menu_id == c_menu_id:
                mess = {"message": "Menu id is exited"}
                return RespHandle.get_resp(mess=mess, code=400)

        menu = Menu(manager_id=manager_id, menu_id=menu_id, menu_name=menu_name, date_create=date_create, describe=describe,
                    menu_pic=menu_pic, categories=categories, items=items)

        menu.save()

        added_menu = Menu.objects().with_id(menu.id)
        resp = jsonify(mlab.item2json(added_menu))
        resp.status_code = 200
        return added_menu.get_json()


class MenuWithMangerID(Resource):
    # get all menu with res id

    def get(self, manager_id):

        try:
            menu = Menu.objects(manager_id=manager_id).first()
            categories = Categoty.objects(menu_id=menu.menu_id)
            # items = Item.objects(menu_id=menu_id)
            items = Item.objects(menu_id=menu.menu_id)

            # temp_cates =[]

            for cate in categories:
                for item in items:
                    if item.cate_id == cate.cate_id:
                        cate.items.append(item)

            menu.categories = categories

            # menu.items = items

        except Exception:
            mess = {"message": "manager not has any menu"}
            return RespHandle.get_resp(mess=mess, code=204)

        return menu.get_json()

    # del all menu with res id

    def delete(self, manager_id):
        menus = Menu.objects(manager_id=manager_id)
        for menu in menus:
            menu.delete()
        return {"message": "del all menu"}, 200
