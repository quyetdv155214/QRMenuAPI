from flask_restful import Resource, reqparse
from model.task import Task
import mlab


class TaskListRes(Resource):
    def get(self):
        tasks = Task.objects()
        task_json = mlab.list2json(tasks)
        return task_json

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name="name", type=str, location="json")
        parser.add_argument(name="local_id", type=str, location="json")

        body = parser.parse_args()

        name = body["name"]
        local_id = body["local_id"]
        task = Task(name=name, local_id=local_id, done=False)
        task.save()

        added_task = Task.objects().with_id(task.id)
        return mlab.item2json(added_task)


class TaskRes(Resource):
    def get(self, task_id):
        task = Task.objects.with_id(task_id)
        return mlab.item2json(task)
