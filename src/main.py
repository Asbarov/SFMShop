class Main:
    def __init__(self,price,quantity):
        self.price=price
        self.quantity=quantity

    def get_total_price(self,price,quantity):
        super().__init__(price,quantity)
        return self.price * self.quantity


class Amir:
    pass

