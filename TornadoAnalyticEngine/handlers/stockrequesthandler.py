import motor
import tornado.web
import json
from utils.cursorserializer import *


# Interface
class StockRequestBrokerI(tornado.web.RequestHandler):
    def initialize(self , database, collection):
        self.db = database
        self.collection = self.db[collection]

        if  self.db is None and self.collection is None:
            raise NotImplementedError




class GetAllStocks(StockRequestBrokerI):
    async def get(self):
        result = []
        async for doc in self.collection.find():
            result.append(doc)
        self.write(CursorEncoder().encode(result))


class GetStockDataBySym(StockRequestBrokerI):
    async def get(self):
        result = []
        symbol = self.get_argument("SYM")
        async for doc in self.collection.find({"dataset.dataset_code": symbol}, {"dataset.data": 1}):
            result.append(doc)
        self.write(CursorEncoder().encode(result))















