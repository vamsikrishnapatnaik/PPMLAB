class Addition:
    def addition(self, a, b):
        return a + b

class Subtraction:
    def subtraction(self, a, b):
        return a - b

class Multiplication:
    def multiplication(self, a, b):
        return a * b

class Division:
    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed"

class Calculator(Addition, Subtraction, Multiplication, Division):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def perform_operations(self):
        print(f"Addition: {self.addition(self.data1, self.data2)}")
        print(f"Subtraction: {self.subtraction(self.data1, self.data2)}")
        print(f"Multiplication: {self.multiplication(self.data1, self.data2)}")
        print(f"Division: {self.division(self.data1, self.data2)}")

data1 = float(input("Enter 1st number : "))
data2 = float(input("Enter 2nd number : "))

calc = Calculator(data1,data2)
calc.perform_operations()