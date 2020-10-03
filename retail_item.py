class RetailItem:
    def __init__(self, description, units_inventory, price):
        self.__item_descpt = description
        self.__units_invent = units_inventory
        self.__price = price

    def set_item_descpt(self, description):
        self.__item_descpt = description
    def set_units_invent(self, units_inventory):
        self.__units_invent = units_inventory
    def set_price(self, price):
        self.__price = price
        
    def get_item_descpt(self):
        return self.__item_descpt
    def get_unit_invent(self):
        return self.__unit_invent
    def get_price(self):
        return self.__price
    
    def __str__(self):
        return 'Item description: ' + self.__item_descpt + '\n' +\
               'Units of inventory: ' + self.__units_invent + '\n' +\
               'Price: ' + self.__price

item1 = RetailItem('jacket', '12', '59.95$')
item2 = RetailItem('designer jeans','40', '34.95$')
item3 = RetailItem('shirt', '20', '24.95$')


print(item1, end = '\n\n')
print(item2, end = '\n\n')
print(item3, end = '\n\n')
