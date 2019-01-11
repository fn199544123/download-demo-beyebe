import datetime
import json

from bson import ObjectId


class CJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, ObjectId):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)
