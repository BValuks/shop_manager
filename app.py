from lib.database_connection import DatabaseConnection
from lib.item_repo import ItemRepository
from lib.order_repo import OrderRepository
from lib.item import Item
from lib.order import Order


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
# connection.seed("seeds/items_orders.sql")
item_repo = ItemRepository(connection)
order_repo = OrderRepository(connection)

print('Welcome to the shop management program!\n')
print('What do you want to do?\n  1 - list all shop items\n  2 - create a new item\n  3 - list all orders\n  4 - create a new order')
print('')
choice = input('- ')

if choice == '1':
    items = item_repo.all()
    print('\nHere is a list of all shop items:\n')
    for item in items:
        print(f'#{item.id} {item.name}:\n  - Unit Price: {item.unit_price}\n  - Quantity: {item.quantity}')

elif choice == '2':
    print('')
    name = input("What is the item's name? ")
    price = input("What is the item's unit price? ")
    quantity = input("What is the item's quantity? ")
    item_repo.create(Item(None, name, price, quantity))
    print(f'{name} has been added with a unit price of {price} and a quantity of {quantity}')

elif choice == '3':
    orders = order_repo.all()
    print('\nHere is a list of all orders:\n')
    for order in orders:
        print(f'#{order.id} Customer name: {order.customer}\n  Date: {order.date}')