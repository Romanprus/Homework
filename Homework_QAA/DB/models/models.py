from pony.orm import Database, PrimaryKey, Required, Optional, Set

db = Database()
db.bind('postgres', user='roman', password='Ringostar999!', host='127.0.0.1', database='store')


class Products(db.Entity):
    _table_ = 'products'
    id = PrimaryKey(int, auto=True)
    name = Required(str, 25)
    price = Required(int)
    order = Set('Orders')


class Orders(db.Entity):
    _table_ = 'orders'
    id = PrimaryKey(int, auto=True)
    quantity = Optional(int)
    products = Required(Products, column="product_id")


db.generate_mapping(create_tables=True)
