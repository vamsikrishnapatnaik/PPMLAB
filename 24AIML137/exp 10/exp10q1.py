class Employee:
    def __init__(self, empid, name, basicPay):
        self.empid = empid
        self.name = name
        self.basicPay = basicPay
        self.ta = 0
        self.da = 0
        self.grosspay = 0.0

    def calc(self):
        self.ta = 0.10 * self.basicPay
        self.da = 0.40 * self.basicPay
        self.grosspay = self.basicPay + self.ta + self.da

    def disp(self):
        print("Employee Details:")
        print(f"ID: {self.empid}")
        print(f"Name: {self.name}")
        print(f"Basic Pay: {self.basicPay}")
        print(f"TA: {self.ta}")
        print(f"DA: {self.da}")
        print(f"Gross Pay: {self.grosspay}")

empid = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
basicPay = float(input("Enter Basic Pay: "))

emp = Employee(empid, name, basicPay)

emp.calc()

emp.disp()