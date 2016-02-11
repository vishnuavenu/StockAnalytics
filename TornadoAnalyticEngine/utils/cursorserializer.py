import json
from bson import ObjectId

class CursorEncoder  (json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ObjectId): # fix for ObjectID encoding error
            return str(obj)
        return json.JSONEncoder.default(self, obj)