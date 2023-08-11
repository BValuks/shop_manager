from lib.item import Item

def test_item_initialise():
    item = Item(1, 'item', 11.11, 1)
    assert item.id == 1
    assert item.name == 'item'
    assert item.unit_price == 11.11
    assert item.quantity == 1

def test_item_formats_nicely():
    item = Item(1, 'item', 11.11, 1)
    assert str(item) == 'Item(1, item, 11.11, 1)'

def test_items_are_same():
    item1 = Item(1, 'item', 11.11, 1)
    item2 = Item(1, 'item', 11.11, 1)
    assert item1 == item2