class OrderError(Exception):
    pass


class OrderSystem:

    def __init__(self):
        self.stock = {"Laptop": 5, "Phone": 3}

    def order(self, product, qty):
        try:
            if product not in self.stock:
                raise OrderError("Product not available")

            if qty > self.stock[product]:
                raise OrderError("Out of stock")

            self.stock[product] -= qty
            print("Order placed")

        except OrderError as e:
            print(e)

    def show_products(self):
        print(self.stock)


o = OrderSystem()

o.order("Laptop", 2)
o.order("Phone", 5)
o.order("TV", 1)
o.show_products()