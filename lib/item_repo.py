from lib.item import Item

class ItemRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM items ORDER BY id ASC')
        items = []
        for row in rows:
            item = Item(row['id'], row['name'], row['unit_price'], row['quantity'])
            items.append(item)
        return items
    
    def find(self, id):
        row = self.connection.execute('SELECT * FROM items WHERE id = %s', [id])
        item = Item(row[0]['id'], row[0]['name'], row[0]['unit_price'], row[0]['quantity'])
        return item
    
    def create(self, item):
        self.connection.execute('INSERT INTO items (name, unit_price, quantity) VALUES (%s, %s, %s)', [item.name, item.unit_price, item.quantity])
    
    def delete(self, id):
        self.connection.execute('DELETE FROM items WHERE id = %s', [id])
    
    def update(self, item):
        self.connection.execute('UPDATE items SET name = %s, unit_price = %s, quantity = %s WHERE id = %s', [item.name, item.unit_price, item.quantity, item.id])