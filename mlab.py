import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds147534.mlab.com:47534/qrcode_db
host = "ds147534.mlab.com"
port = 47534
db_name = "qrcode_db"
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
