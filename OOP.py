class Student:
    collage_name = "DKTE collge" #class variable

    def __init__(self, fullName, marks):
        self.name = fullName #instance variable
        self.marks = marks
        print("Constructor called")
    def hello(self):#methods = the function inside the class
        print("Hello Students")
    def get_marks(self):
        return self.marks 

s1 = Student("Aarya", 97)
print(s1.name)
print(s1.marks)
print(s1.collage_name)
print(s1.hello())
print(s1.get_marks())
s2 = Student("Shreeja",99)
print(s2.name)
print(s2.marks)
print(s2.collage_name)




"""class Car:
    color = "Red"
    model = "2020"
    brand = "Toyota"

c1 = Car()
print(c1.color)
print(c1.model)
print(c1.brand)"""


"""class Student2:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
    def get_average(self):
        return sum(self.marks)/len(self.marks)



s2 = Student2("Aarti",[99, 98, 97])
print("Average :", s2.get_average())"""

#OR


class Student2:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        total = 0
        for i in self.marks:
            total += i
        avg = total / len(self.marks)
        return avg


s2 = Student2("Aarti", [99, 98, 97])

print("Average :", s2.get_average())

#static method
# static methods are the  methods does not need self parameter and work at class level
class Math:
    @staticmethod
    def add(a,b):
        return a + b
    
m1 = Math()
print(m1.add(5,10))

#abstraction

#del keyword
class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("aarti")
print(s1.name)
del s1.name
#print(s1.name) #AttributeError: 'Student' object has no attribute 'name'

#private attribute
class account:
    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

a1 = account(12345, "mypassword")
print(a1.acc_no)
#print(a1.__acc_pass) #AttributeError: 'account' object has no attribute '__acc_pass'


class Car:
    color = "Black"
    @staticmethod
    def Start():
        print("Car Started")
    def Stop():
        print("Car stopped")
    
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
c1 = ToyotaCar("Fortuner")
c2 = ToyotaCar("Prius")
print(c1.Start())
print(c1.color)

#single inheritance
#multileval inheritance
#multiple inheritance
class A:
    varA = "Welcome to class A"
class B:
    varB = "Welcome to class B"
class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

#Super method
#uesd to access the method of parent class
class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car Stoped")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

car1 = ToyotaCar("Fortunier","Electric")
print(car1.type)

#polymorphism
#Operator overloding
#when the operator is akllowd to have diff meaning according to the context
print(1 + 2) # basic addition 
print("Arti" + "Shintre") # conacatination
print([1, 2, 3] + [4, 5, 6]) #merge list 

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showNum(self):
        print(self.real,"i +",self.img,"j")
    def __add__(num1, num2):
        newReal = num1.real + num2.real
        newImg = num1.img + num2.img
        return Complex(newReal , newImg)


num1 = Complex(1, 3)
num1.showNum()

num2 = Complex(2, 4)
num2.showNum()

#num3 = num1.add(num2)
#if i dont want these syntax .add then i use dunder functions
num3 = num1 + num2

num3.showNum()
