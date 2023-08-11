from lib.item_repo import ItemRepository
from lib.item import Item

def test_all(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repo = ItemRepository(db_connection)
    result = repo.all()
    assert result == [
        Item(1, 'Maton Acoustic', 2345.99, 3),
        Item(2, 'Tanglewood Acoustic', 679.49, 6),
        Item(3, 'Eastman Mandolin', 659.00, 4),
        Item(4, 'Kala Baritone Ukulele', 519.49, 5),
        Item(5, 'Elixir Strings', 11.99, 20),
        Item(6, 'Strap', 14.99, 15),
        Item(7, 'Snark Tuner', 19.99, 15),
        Item(8, 'Dusty Bread Roll', 1.19, 1)
    ]


def test_find(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repo = ItemRepository(db_connection)
    result = repo.find(8)
    assert result == Item(8, 'Dusty Bread Roll', 1.19, 1)

def test_create(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repo = ItemRepository(db_connection)
    assert repo.create(Item(None, 'Dustier Bread Roll', 4.99, 1)) == None
    assert repo.all() == [
        Item(1, 'Maton Acoustic', 2345.99, 3),
        Item(2, 'Tanglewood Acoustic', 679.49, 6),
        Item(3, 'Eastman Mandolin', 659.00, 4),
        Item(4, 'Kala Baritone Ukulele', 519.49, 5),
        Item(5, 'Elixir Strings', 11.99, 20),
        Item(6, 'Strap', 14.99, 15),
        Item(7, 'Snark Tuner', 19.99, 15),
        Item(8, 'Dusty Bread Roll', 1.19, 1),
        Item(9, 'Dustier Bread Roll', 4.99, 1)
    ]

def test_delete(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repo = ItemRepository(db_connection)
    assert repo.delete(9) == None
    assert repo.all() == [
        Item(1, 'Maton Acoustic', 2345.99, 3),
        Item(2, 'Tanglewood Acoustic', 679.49, 6),
        Item(3, 'Eastman Mandolin', 659.00, 4),
        Item(4, 'Kala Baritone Ukulele', 519.49, 5),
        Item(5, 'Elixir Strings', 11.99, 20),
        Item(6, 'Strap', 14.99, 15),
        Item(7, 'Snark Tuner', 19.99, 15),
        Item(8, 'Dusty Bread Roll', 1.19, 1)
    ]

def test_update(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    repo = ItemRepository(db_connection)
    item = repo.find(5)
    item.unit_price = 14.99
    assert repo.update(item) == None
    assert repo.all() == [
        Item(1, 'Maton Acoustic', 2345.99, 3),
        Item(2, 'Tanglewood Acoustic', 679.49, 6),
        Item(3, 'Eastman Mandolin', 659.00, 4),
        Item(4, 'Kala Baritone Ukulele', 519.49, 5),
        Item(5, 'Elixir Strings', 14.99, 20),
        Item(6, 'Strap', 14.99, 15),
        Item(7, 'Snark Tuner', 19.99, 15),
        Item(8, 'Dusty Bread Roll', 1.19, 1)
    ]