from datetime import datetime

from src.customer import Customer
from src.item import Item


class Basket(object):

    def __init__(self, number_of_items):
        start = 0
        sum_prices = 0
        item_list = []
        while start < number_of_items:
            item_list.append(Item())
            start += 1
        for thing in item_list:
            sum_prices = sum_prices + thing.price
        self.customer = Customer()
        self.items = item_list
        self.total_price = sum_prices
        self.date_created = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
