from typing import Dict
from pymongo import MongoClient

class Database:
  URI = 'mongodb://127.0.0.1:27017/'
  # URI = 'mongodb+srv://dev:shoppinggenie@sg-database-gwpru.mongodb.net/test'
  DATABASE = MongoClient(URI).get_database()

  @staticmethod
  def insert(collection: str, data: Dict):
    Database.DATABASE[collection].insert(data)
