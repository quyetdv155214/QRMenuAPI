from flask_restful import Resource, reqparse
from model.menu import Menu
from model.item import Item
import mlab


class MenuRes(Resource):
    def get(self, menu_id):
        menu = Menu.objects().with_id(menu_id)
        menu_json = mlab.item2json(menu)
        return menu_json

    def put(self, menu_id):
        menu = Menu.objects().with_id(menu_id)
        parser = reqparse.RequestParser()
        parser.add_argument(name="menu_id", type=str, location="json")
        parser.add_argument(name="menu_name", type=str, location="json")
        parser.add_argument(name="menu_category", type=str, location="json", action='append')

    def delete(self, menu_id):
        try:
            menu = Menu.objects().with_id(menu_id)
        except Exception:
            pass
        if menu is None:
            return {"status": 404, "message": "menu not found !"}
        else:
            menu.delete()
            return {"status": 200, "message": "delete success"}


class MenuLisRes(Resource):
    def get(self):
        menu = Menu.objects()
        menu_json = mlab.list2json(menu)
        return menu_json

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name="menu_id", type=str, location="json")
        parser.add_argument(name="menu_name", type=str, location="json")
        parser.add_argument(name="menu_category", type=str, location="json", action='append')

        body = parser.parse_args()

        menu_id = body["menu_id"]
        menu_name = body["menu_name"]
        menu_category = body["menu_category"]

        menu = Menu(menu_id=menu_id, menu_name=menu_name, menu_category=menu_category)

        menu.save()

        added_menu = Menu.objects().with_id(menu.id)
        return mlab.item2json(added_menu)