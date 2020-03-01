from models.item import Item

url = 'https://www.bestbuy.com/site/apple-macbook-pro-16-display-with-touch-bar-intel-core-i9-16gb-memory-amd-radeon-pro-5500m-1tb-ssd-latest-model-space-gray/6366572.p?skuId=6366572'
tag_name = 'div'
query = {'class': 'pricing-lib-price-7-2006-8 price-view-pb priceView-layout-large'}

ipad = Item(url, tag_name, query)
ipad.save_to_mongo()
# items_loaded = Item.all()
# print(items_loaded)
# print(items_loaded[0].load_price())





