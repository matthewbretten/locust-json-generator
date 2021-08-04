from locust import HttpUser, task
from src.basket import Basket
import jsons


class CommerceCustomer(HttpUser):

    @task
    def post_new_basket(self):
        payload = jsons.dumps(Basket(2))
        self.client.post("/basket", data=payload)
