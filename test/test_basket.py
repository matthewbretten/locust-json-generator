from src.basket import Basket


def test_basket_size():
    basket = Basket(2).__dict__
    assert len(basket['items']) == 2


def test_basket_total_price():
    basket = Basket(2).__dict__
    total_price = 0
    for item in basket['items']:
        total_price = total_price + item.price
    assert basket['total_price'] == total_price