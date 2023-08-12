from lib.order import Order
from lib.item import Item

class OrderRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM orders ORDER BY id ASC')
        orders = [Order(row['id'], row['customer'], row['date']) for row in rows]
        # for row in rows:
        #     item = Order(row['id'], row['customer'], row['date'])
        #     orders.append(item)
        return orders
    
    def find(self, id):
        row = self.connection.execute('SELECT * FROM orders WHERE id = %s', [id])
        order = Order(row[0]['id'], row[0]['customer'], row[0]['date'])
        return order
    
    def find_by_item(self, item):
        rows = self.connection.execute('SELECT orders.id AS "order_id", orders.customer, orders.date, items.id AS "item_id", items.name, items.unit_price, items.quantity FROM orders JOIN items_orders ON items_orders.order_id = orders.id JOIN items ON items_orders.item_id = items.id WHERE items.name = %s', [item])
        orders = [Order(row['order_id'], row['customer'], row['date']) for row in rows]
        return Item(rows[0]['item_id'], rows[0]['name'], rows[0]['unit_price'], rows[0]['quantity'], orders)
    
    def create(self, order):
        id = self.connection.execute('INSERT INTO orders (customer, date) VALUES (%s, %s) RETURNING id', [order.customer, order.date])
        return id[0]['id']
    
    def delete(self, id):
        self.connection.execute('DELETE FROM orders WHERE id = %s', [id])

    def update(self, order):
        self.connection.execute('UPDATE orders SET customer = %s, date = %s WHERE id = %s', [order.customer, order.date, order.id])