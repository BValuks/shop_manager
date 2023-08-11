from lib.order_repo import OrderRepository
from lib.order import Order
import datetime

def test_all(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repo = OrderRepository(db_connection)   
    result = repo.all()
    assert result == [
        Order(1, 'Benedict', datetime.date(2023, 5, 30)),
        Order(2, 'Will', datetime.date(2022, 7, 4)),
        Order(3, 'Ian', datetime.date(2023, 3, 18)),
        Order(4, 'Simeon', datetime.date(2022, 10, 16)),
        Order(5, 'Megan', datetime.date(2023, 6, 21))
    ]

def test_find(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repo = OrderRepository(db_connection)
    result = repo.find(4)
    assert result == Order(4, 'Simeon', datetime.date(2022, 10, 16))

def test_create(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repo = OrderRepository(db_connection)
    assert repo.create(Order(None, 'Benedict', datetime.date(2023, 8, 11))) == None
    assert repo.all() == [
        Order(1, 'Benedict', datetime.date(2023, 5, 30)),
        Order(2, 'Will', datetime.date(2022, 7, 4)),
        Order(3, 'Ian', datetime.date(2023, 3, 18)),
        Order(4, 'Simeon', datetime.date(2022, 10, 16)),
        Order(5, 'Megan', datetime.date(2023, 6, 21)),
        Order(6, 'Benedict', datetime.date(2023, 8, 11))
    ]

def test_delete(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repo = OrderRepository(db_connection)
    assert repo.delete(6) == None
    assert repo.all() == [
        Order(1, 'Benedict', datetime.date(2023, 5, 30)),
        Order(2, 'Will', datetime.date(2022, 7, 4)),
        Order(3, 'Ian', datetime.date(2023, 3, 18)),
        Order(4, 'Simeon', datetime.date(2022, 10, 16)),
        Order(5, 'Megan', datetime.date(2023, 6, 21))
    ]

def test_update(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repo = OrderRepository(db_connection)
    order = repo.find(3)
    order.date = datetime.date(2023, 3, 27)
    assert repo.update(order) == None
    assert repo.all() == [
        Order(1, 'Benedict', datetime.date(2023, 5, 30)),
        Order(2, 'Will', datetime.date(2022, 7, 4)),
        Order(3, 'Ian', datetime.date(2023, 3, 27)),
        Order(4, 'Simeon', datetime.date(2022, 10, 16)),
        Order(5, 'Megan', datetime.date(2023, 6, 21))
    ]