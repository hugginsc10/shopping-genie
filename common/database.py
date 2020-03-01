import os
from typing import Dict
import pymongo

class Database:
  #URI = 'mongodb://127.0.0.1:27017/'
  URI = 'mongodb+srv://dev:shoppinggenie@sg-database-gwpru.mongodb.net/sg-db'
  DATABASE = pymongo.MongoClient(URI).get_default_database()

  @staticmethod
  def insert(collection: str, data: Dict):
    Database.DATABASE[collection].insert(data)
