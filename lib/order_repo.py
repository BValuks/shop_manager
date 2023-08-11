from lib.order import Order

class OrderRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM orders ORDER BY id ASC')
        orders = []
        for row in rows:
            item = Order(row['id'], row['customer'], row['date'])
            orders.append(item)
        return orders
    
    def find(self, id):
        row = self.connection.execute('SELECT * FROM orders WHERE id = %s', [id])
        order = Order(row[0]['id'], row[0]['customer'], row[0]['date'])
        return order
    
    def create(self, order):
        self.connection.execute('INSERT INTO orders (customer, date) VALUES (%s, %s)', [order.customer, order.date])
    
    def delete(self, id):
        self.connection.execute('DELETE FROM orders WHERE id = %s', [id])

    def update(self, order):
        self.connection.execute('UPDATE orders SET customer = %s, date = %s WHERE id = %s', [order.customer, order.date, order.id])