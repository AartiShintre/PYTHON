class Bank:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print("RS.",amount,"was debited from your account")
        print("Total balance is : ", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("RS.",amount,"was credited to your account")
        print("Total balance is : ", self.balance)
    def print_balance(self):
        return self.balance

b1 = Bank(5000, "abc123")
b1.debit(1000)
b1.credit(2000)
b1.print_balance()


#WAP define a circle class to create a circle with radius r using the constructor define area method of the class which calculate the area of a circle define the peimeter method which calculate the perimeter

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return (22/7) * self.radius ** 2
    def Perimeter(self):
        return 2 * (22/7)* self.radius
c1 = Circle(21)
print(c1.area())
print(c1.Perimeter())

#WAP
class Employee:
    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal
    def showDetails(self):
        print("Role : ",self.role)
        print("Department : ",self.dept)
        print("Salary : ",self.sal)
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","200000")

engg1 = Engineer("Arti","20")
print(engg1.showDetails())

#WAP
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
o1 = Order("Chips",10)
o2 = Order("Tea",20)
