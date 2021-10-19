import json
from bson.json_util import dumps

def toJson(collection):
   if isinstance(collection, list):
      list_collection = list(collection)
      return json.loads(dumps(list_collection))
   return json.loads(dumps(collection))
