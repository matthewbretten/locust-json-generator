import random

from src.customers import Customers


class Customer(object):

    def __init__(self):
        customer = random.choice(Customers().customers)
        self.name = customer['name']
        self.age = customer['age']
        self.country_code = customer['country_code']
