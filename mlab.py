import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds121980.mlab.com:21980/a7-dummy
host = "ds121980.mlab.com"
port = 21980
db_name = "a7-dummy"
username = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)


def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
