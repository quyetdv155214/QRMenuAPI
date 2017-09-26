from flask import Flask
import mlab
from model.task import Task
from flask_restful import Api
from resources.task_resource import *

mlab.connect()
app = Flask(__name__)

api = Api(app)

all_tasks = Task.objects()

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

api.add_resource(TaskListRes, "/tasks")
api.add_resource(TaskRes, "/tasks/<task_id>")
if __name__ == '__main__':
    app.run()
