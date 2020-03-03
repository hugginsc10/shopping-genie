from typing import Dict
from bs4 import BeautifulSoup
import requests
import re
import uuid
from common.database import Database
class Item:
  def __init__(self, url: str, tag_name: str, query: Dict, _id: str = None):
    super().__init__()
    self.url = url
    self.tag_name = tag_name
    self.query = query
    self.price = None
    self.collection = "items"
    self._id = uuid.uuid4().hex
    self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
 
  def __repr__(self):
    return f"<Item {self.url}>"

  def load_price(self) -> float:
    response = requests.get(self.url, headers=self.header, timeout=5)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    element = soup.find(self.tag_name, self.query)
    price_string = re.findall(r"\$\d+(?:\,\d+\.\d+)?", element.text)

    pattern = re.compile(r"(\d+,?\d*\.\d\d)")
    match = pattern.search(price_string[0])

    found_price = match.group(1)
    without_commas = found_price.replace(",", "")
    self.price = float(without_commas)

    return self.price

  def json(self) -> Dict:
    return {
      "_id": self._id,
      "url": self.url,
      "tag_name": self.tag_name,
      "query": self.query
    }
    
  @classmethod
  def all(cls):
    items_from_db = Database.find('items', {})
    return [Item(**item) for item in items_from_db]
  def save_to_mongo(self) -> None:
    Database.insert(self.collection, self.json())

  