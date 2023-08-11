from lib.order import Order

def test_order_initialise():
    order = Order(1, 'customer', '1990-05-30')
    assert order.id == 1
    assert order.customer == 'customer'
    assert order.date == '1990-05-30'

def test_order_formats_nicely():
    order = Order(1, 'customer', '1990-05-30')
    assert str(order) == 'Order(1, customer, 1990-05-30)'

def test_orders_are_same():
    order1 = Order(1, 'customer', '1990-05-30')
    order2 = Order(1, 'customer', '1990-05-30')
    assert order1 == order2