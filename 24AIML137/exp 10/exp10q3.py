

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_amount = 0 

    def calculate_total(self):
        self.total_amount = self.price * self.quantity

    def disp(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.name)
        print("Price: ₹", self.price)
        print("Quantity:", self.quantity)
        print("Total Amount: ₹", self.total_amount)
        print("---------------------------")


if __name__ == "__main__":
    p1 = Product(101, "Milk", 45.50, 2)
    p2 = Product(102, "Bread", 30.00, 3)

    p1.calculate_total()
    p2.calculate_total()

    p1.disp()
    p2.disp()