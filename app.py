from lib.database_connection import DatabaseConnection
from lib.item_repo import ItemRepository
from lib.order_repo import OrderRepository
from lib.item import Item
from lib.order import Order
from datetime import date


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
# connection.seed("seeds/items_orders.sql")
item_repo = ItemRepository(connection)
order_repo = OrderRepository(connection)

print('Welcome to the shop management program!\n')
print('What do you want to do?\n  1 - list all shop items\n  2 - create a new item\n  3 - update item\n  4 - delete item\n  5 - list all orders\n  6 - create a new order')
print('')
choice = input('- ')

if choice == '1': # list all shop items
    items = item_repo.all()
    print('\nHere is a list of all shop items:\n')
    for item in items:
        print(f'#{item.id} {item.name}:\n  - Unit Price: {item.unit_price}\n  - Quantity: {item.quantity}')

elif choice == '2': # create a new item
    print('')
    name = input("What is the item's name? ")
    price = input("What is the item's unit price? ")
    quantity = input("What is the item's quantity? ")
    item_repo.create(Item(None, name, price, quantity))
    print(f'{name} has been added with a unit price of {price} and a quantity of {quantity}')

elif choice == '3': # update item
    print('')
    item_choice = input('What item would you like to update? ')
    item = item_repo.find_by_name(item_choice)

    choice_name = input('Would you like to update the name? (Y/N) ')
    if choice_name.lower() == 'y':
        new_name = input('What name would you like to give the item? ')
        item.name = new_name

    choice_price = input('Would you like to update the unit price? (Y/N) ')
    if choice_price.lower() == 'y':
        new_price = input('What would you like the unit price to be? ')
        item.unit_price = float(new_price)

    choice_quantity = input('Would you like to update the quantity? (Y/N) ')
    if choice_quantity.lower() == 'y':
        new_quantity = input('What would you like the quantity to be? ')
        item.quantity = int(new_quantity)
    
    item_repo.update(item)
    print(f'{item_choice} has been updated')

elif choice == '4': # delete item
    print('')
    item = input('Which item would you like to delete? ')
    item_repo.delete_by_name(item)
    print(f'{item} has been deleted from shop items list')

elif choice == '5': # list all orders
    orders = order_repo.all()
    print('\nHere is a list of all orders:\n')
    for order in orders:
        print(f'#{order.id} Customer name: {order.customer}\n  Date: {order.date}')
    
elif choice == '6': # create a new order
    print('')
    customer = input('\nWhat is the customer name?\n')
    order_id = order_repo.create(Order(None, customer, date.today()))
    items = []
    number_of_items = input('\nHow many items in the order? ')
    print('')
    for i in range(int(number_of_items)):
        item = input(f'Item {i + 1}: ')
        object = item_repo.find_by_name(item)
        items.append(object)
    for item in items:
        connection.execute('INSERT INTO items_orders (item_id, order_id) VALUES (%s, %s)', [item.id, order_id])
    print('Order has been added')