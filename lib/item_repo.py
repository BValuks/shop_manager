from lib.item import Item
from lib.order import Order

class ItemRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM items ORDER BY id ASC')
        items = [Item(row['id'], row['name'], row['unit_price'], row['quantity']) for row in rows]
        # for row in rows:
        #     item = Item(row['id'], row['name'], row['unit_price'], row['quantity'])
        #     items.append(item)
        return items
    
    def find(self, id):
        row = self.connection.execute('SELECT * FROM items WHERE id = %s', [id])
        item = Item(row[0]['id'], row[0]['name'], row[0]['unit_price'], row[0]['quantity'])
        return item
    
    def find_by_name(self, name):
        row = self.connection.execute('SELECT * FROM items WHERE name = %s', [name])
        item = Item(row[0]['id'], row[0]['name'], row[0]['unit_price'], row[0]['quantity'])
        return item
    
    def find_by_order(self, order_id):
        rows = self.connection.execute('SELECT items.id AS "item_id", items.name, items.unit_price, items.quantity, orders.id AS "order_id", orders.customer, orders.date FROM items JOIN items_orders ON items_orders.item_id = items.id JOIN orders ON items_orders.order_id = orders.id WHERE orders.id = %s', [order_id])
        items = [Item(row['item_id'], row['name'], row['unit_price'], row['quantity']) for row in rows]
        # for row in rows:
        #     item = Item(row['item_id'], row['name'], row['unit_price'], row['quantity'])
        #     items.append(item)
        return Order(rows[0]['order_id'], rows[0]['customer'], rows[0]['date'], items)
    
    def create(self, item):
        self.connection.execute('INSERT INTO items (name, unit_price, quantity) VALUES (%s, %s, %s)', [item.name, item.unit_price, item.quantity])
    
    def delete(self, id):
        self.connection.execute('DELETE FROM items WHERE id = %s', [id])
    
    def delete_by_name(self, name):
        self.connection.execute('DELETE FROM items WHERE name = %s', [name])
    
    def update(self, item):
        self.connection.execute('UPDATE items SET name = %s, unit_price = %s, quantity = %s WHERE id = %s', [item.name, item.unit_price, item.quantity, item.id])