from flask_restful import Resource, reqparse
from model.menu import Menu
from model.item import Item
from datetime import datetime
from util.resp_handle import *
from flask import jsonify

import mlab


class MenuWithID(Resource):
    def get(self, menu_id):
        try:
            menu = Menu.objects().with_id(menu_id)
        except Exception:
            mess = {"message": "menu id not exit"}
            return RespHandle.get_resp(mess=mess, code=204)
        menu_json = mlab.item2json(menu)
        return menu_json

    def put(self, menu_id):
        menu = Menu.objects().with_id(menu_id)
        parser = reqparse.RequestParser()
        # add argument
        parser.add_argument(name="res_id", type=str, location="json")
        parser.add_argument(name="menu_id", type=str, location="json")
        parser.add_argument(name="menu_name", type=str, location="json")
        parser.add_argument(name="describe", type=str, location="json")
        # parse body
        body = parser.parse_args()
        # getdata from body
        res_id = body["res_id"]
        menu_id = body["menu_id"]
        menu_name = body["menu_name"]
        # date_create = menu["date_create"]
        describe = body["describe"]

        # check require field
        if res_id is None:
            mess = {"message": "Restaurant id is required"}
            return RespHandle.get_resp(mess=mess, code=400)
        if menu_id is None:
            mess = {"message": "Menu id is required"}
            return RespHandle.get_resp(mess=mess, code=400)

        curent_menus = Menu.objects()
        # check exit id
        for m in curent_menus:
            # c_res_id = m["res_id"]
            c_menu_id = m["menu_id"]
            # if res_id == c_res_id:
            #     mess = {"message": "Restaurant id is exited"}
            #     return RespHandle.get_resp(mess=mess, code=400)

            if menu_id == c_menu_id:
                mess = {"message": "Menu id is exited"}
                return RespHandle.get_resp(mess=mess, code=400)

        menu.update(set__res_id=res_id, set__menu_id=menu_id, set__menu_name=menu_name, set__describe=describe)

        edited_menu = Menu.objects().with_id(menu.id)
        resp = jsonify(mlab.item2json(edited_menu))
        resp.status_code = 200
        return {resp}

    def delete(self, menu_id):
        try:
            menu = Menu.objects().with_id(menu_id)
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
        parser.add_argument(name="res_id", type=str, location="json")
        parser.add_argument(name="menu_id", type=str, location="json")
        parser.add_argument(name="menu_name", type=str, location="json")
        parser.add_argument(name="date_create", type=str, location="json")
        parser.add_argument(name="describe", type=str, location="json")

        # parse body
        body = parser.parse_args()
        # getdata from body
        res_id = body["res_id"]
        menu_id = body["menu_id"]
        menu_name = body["menu_name"]
        date_create = datetime.strptime(body["date_create"], "%d/%m/%y")  # "21/11/06 16:30", "%d/%m/%y %H:%M"
        describe = body["describe"]

        curent_menus = Menu.objects()
        # check require field
        if res_id is None:
            mess = {"message": "Restaurant id is required"}
            return RespHandle.get_resp(mess=mess, code=400)
        if menu_id is None:
            mess = {"message": "Menu id is required"}
            return RespHandle.get_resp(mess=mess, code=400)

        # check exit id
        for m in curent_menus:
            # c_res_id = m["res_id"]
            c_menu_id = m["menu_id"]

            if menu_id == c_menu_id:
                mess = {"message": "Menu id is exited"}
                return RespHandle.get_resp(mess=mess, code=400)

        menu = Menu(res_id=res_id, menu_id=menu_id, menu_name=menu_name, date_create=date_create, describe=describe)

        menu.save()

        added_menu = Menu.objects().with_id(menu.id)
        resp = jsonify(mlab.item2json(added_menu))
        resp.status_code = 200
        return mlab.item2json(added_menu)


class MenuWithResID(Resource):
    # get all menu with res id

    def get(self, res_id):
        menus = Menu.objects(res_id=res_id)
        return mlab.list2json(menus), 200

    # del all menu with res id

    def delete(self, res_id):
        menus = Menu.objects(res_id=res_id)
        for menu in menus:
            menu.delete()
        return {"message":"del all menu"},200

