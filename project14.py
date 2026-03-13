class OutOfStockError(Exception):
    pass


class InvalidProductIDError(Exception):
    pass


class Inventory:

    def __init__(self):
        self.products = {"101": 10, "102": 5}

    def sell_product(self, pid, qty):
        try:
            if pid not in self.products:
                raise InvalidProductIDError("Invalid product ID")

            if qty > self.products[pid]:
                raise OutOfStockError("Not enough stock")

            self.products[pid] -= qty
            print("Product sold")

        except (OutOfStockError, InvalidProductIDError) as e:
            print(e)

    def display(self):
        print(self.products)


i = Inventory()

i.sell_product("101", 3)
i.sell_product("105", 2)
i.sell_product("102", 10)

i.display()