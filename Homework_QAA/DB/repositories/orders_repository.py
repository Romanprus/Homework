from pony.orm import db_session

from Homework_QAA.DB.models.models import Orders


class OrderRepository:
    def __init__(self):
        self.__model = Orders

    @db_session
    def add_order(self, quantity, products):
        self.__model(quantity=quantity, products=products)


if __name__ == '__main__':
    order_repo = OrderRepository()
    order_repo.add_order(50, products=1)
    order_repo.add_order(100, products=2)
    order_repo.add_order(150, products=3)
    order_repo.add_order(200, products=4)
