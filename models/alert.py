import uuid
from typing import Dict, List
from models.item import Item


class Alert:
  def __init__(self, item_id: str, price_limit: float, _id: str = None):
    self.item_id = item_idself
    self.item = Item.get_by_id(item_id)
    self.price_limit = price_limit
    self.collection = "alerts"
    self._id = _id or uuid.uuid4().hex

  def json(self):
    pass

  def save_to_mongo(self):
    pass

  def load_item_price(self):
    pass

  def notify_if_price_reached(self):
    pass

  @classmethod
  def all(cls) -> List:
    pass