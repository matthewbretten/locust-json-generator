from random import choice
from src.items import Items


class Item(object):
    def __init__(self):
        item = choice(Items().items)
        self.basket_item_id = item['basket_item_id']
        self.description = item['description']
        self.price = item['price']
