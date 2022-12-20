from Homework_QAA.DB.models.models import Products
from pony.orm import db_session, left_join

class ProductRepository():
    def __init__(self):
        self.__model = Products

    @db_session
    def add_product(self, name, price):
        self.__model(name=name, price=price)

    @db_session
    def left_join(self):
         results = left_join((products, orders) for products in self.__model for orders in products.orders)
         for result in results:
             products = result[0]
             orders = result[1]
             print(f"id: {products.id}, name: {products.name}, price:{products.price} quantity: {orders.quantity}, "
                   f"total: {products.price * orders.quantity}")


 if __name__ == '__main__':
     product_repo = ProductRepository()
     product_repo.add_product('PC', 2000)
     product_repo.add_product('X-box', 1500)
     product_repo.add_product('PlayStation', 1000)
     product_repo.add_product('Nokia', 5000)
     product_repo.add_product('FunnyGun', 1000)
     product_repo.left_join()