class Order:
    def __init__(self, id, customer, date, items=None):
        self.id = id
        self.customer = customer
        self.date = date
        self.items = items or []
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Order({self.id}, {self.customer}, {self.date})'