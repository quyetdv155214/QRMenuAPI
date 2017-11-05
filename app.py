from flask import Flask
import mlab
from flask_restful import Api
from resources.menu_resource import *
from resources.category_resource import *
from resources.restaurant_resource import *
from resources.item_resource import *
from resources.manager_acc_resource import *
mlab.connect()
app = Flask(__name__)

api = Api(app)


# for task in all_tasks:
#     print(mlab.item2json(task))
#
# my_task = Task.objects(name="aaa").first()
# print(mlab.item2json(my_task))
#
# my_task.update(set__done=False)
# print(mlab.item2json(my_task))
#
# my_task.delete()


# api.add_resource(MenuRes, "/menu")
api.add_resource(MenuWithID, "/menu_id/<menu_id>")
api.add_resource(Menus, "/menu")
api.add_resource(RestaurantRes, "/restaurant")
api.add_resource(EditRestaurant, "/edit_restaurant/<res_id>")
api.add_resource(MenuWithMangerID, "/menu_manager/<manager_id>")
api.add_resource(CategoryRes, "/category")
api.add_resource(CateoryWithID, "/category_id/<cate_id>")
api.add_resource(CategoryWithMenu, "/category_menu_id/<menu_id>")
api.add_resource(ItemRes, "/item")
api.add_resource(ItemWithID, "/item/<item_id>")
api.add_resource(ItemWithMenuId, "/item_menu/<menu_id>")
api.add_resource(ViewCount, "/itemview/<item_id>")
api.add_resource(ManagerLogin, "/mlogin")
api.add_resource(ManagerRegister, "/mRegister")



if __name__ == '__main__':
    app.run()
