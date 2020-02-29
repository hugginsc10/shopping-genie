import requests

response = requests.get("https://www.bestbuy.com/site/apple-macbook-pro-16-display-with-touch-bar-intel-core-i9-16gb-memory-amd-radeon-pro-5500m-1tb-ssd-latest-model-space-gray/6366572.p?skuId=6366572")

print(response.content)