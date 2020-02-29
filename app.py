import requests
from bs4 import BeautifulSoup
import time
import sys
import os
import math
import random
import re
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

URL = 'https://www.bestbuy.com/site/apple-macbook-pro-16-display-with-touch-bar-intel-core-i9-16gb-memory-amd-radeon-pro-5500m-1tb-ssd-latest-model-space-gray/6366572.p?skuId=6366572'
TAG_NAME = 'div'
QUERY = {'class': 'pricing-lib-price-7-2006-8 price-view-pb priceView-layout-large'}

response = requests.get(URL, headers=header, timeout=5)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
element = soup.find(TAG_NAME, QUERY)
price_string = re.findall(r"\$\d+(?:\,\d+\.\d+)?", element.text)


print(price_string[0])





