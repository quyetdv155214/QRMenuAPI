from flask import jsonify


class RespHandle:

    def get_resp(mess, code):
        resp = jsonify(mess)
        resp.status_code = code
        return resp
