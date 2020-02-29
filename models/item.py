import re
import requests
from bs4 import BeautifulSoup
import random
import math
import os
import sys
import time

class Item:
  def __init__(self, url, tag_name, query):
    self.url = url
    self.tag_name = tag_name
    self.query = query
    self.price = None
  def load_price(self):
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    response = requests.get(self.url, headers=header, timeout=5)
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
