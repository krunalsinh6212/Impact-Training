# # Object Oriented Programming
# class Animals:
#     def __init__(self, name):
#         self.name = name
#         self.legs = 4
#     def speaks(self):
#         print(f"{self.name} : barks!!!")
# mydog = Animals("Rocky")
# mydog.speaks()
# print(mydog.legs)

# # Single Inheritance 
# class Fruits:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#     def taste(self):
#         print(f"{self.name} tastes sweet !!!")
# class Mango(Fruits):
#     def __init__(self, name, color):
#         super().__init__(name, color)
#         self.size = 10
# My_mango = Mango("Hapus", "Yellow")
# My_mango.taste()

# Abstraction
from abc import ABC, abstractmethod

# Abstract Class
# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         """Method to calculate the area of the shape"""
#         pass

#     @abstractmethod
#     def perimeter(self):
#         """Method to calculate the perimeter of the shape"""
#         pass

# # Subclass of Shape
# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth

#     def perimeter(self):
#         return 2 * (self.length + self.breadth)

# # Subclass of Shape
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14159 * self.radius * self.radius

#     def perimeter(self):
#         return 2 * 3.14159 * self.radius

# # Attempting to create an instance of Shape will result in an error
# # shape = Shape()  # TypeError: Can't instantiate abstract class Shape

# # Using subclasses
# rect = Rectangle(10, 5)
# print("Rectangle Area:", rect.area())
# print("Rectangle Perimeter:", rect.perimeter())

# circle = Circle(7)
# print("Circle Area:", circle.area())
# print("Circle Perimeter:", circle.perimeter())

# from abc import ABC, abstractmethod

# # Abstract Class
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         """Method to start the vehicle"""
#         pass

#     @abstractmethod
#     def stop(self):
#         """Method to stop the vehicle"""
#         pass

#     @abstractmethod
#     def fuel_type(self):
#         """Method to return the type of fuel the vehicle uses"""
#         pass

# # Subclass: Car
# class Car(Vehicle):
#     def start(self):
#         print("Car is starting...")

#     def stop(self):
#         print("Car is stopping...")

#     def fuel_type(self):
#         return "Petrol"

# # Subclass: Bike
# class Bike(Vehicle):
#     def start(self):
#         print("Bike is starting...")

#     def stop(self):
#         print("Bike is stopping...")

#     def fuel_type(self):
#         return "Diesel"

# # Subclass: ElectricScooter
# class ElectricScooter(Vehicle):
#     def start(self):
#         print("Electric Scooter is starting silently...")

#     def stop(self):
#         print("Electric Scooter is stopping...")

#     def fuel_type(self):
#         return "Electric Battery"

# # Instantiating Subclasses
# car = Car()
# car.start()
# print("Car Fuel Type:", car.fuel_type())
# car.stop()

# print("-" * 20)

# bike = Bike()
# bike.start()
# print("Bike Fuel Type:", bike.fuel_type())
# bike.stop()

# print("-" * 20)

# scooter = ElectricScooter()
# scooter.start()
# print("Scooter Fuel Type:", scooter.fuel_type())
# scooter.stop()

# from abc import ABC, abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def make_payment(self, amount):
#         """Abstract method to process payment."""
#         pass

# class CreditCardPayment(Payment):
#     def make_payment(self, amount):
#         return f"Payment of ${amount} made using Credit Card."

# class PayPalPayment(Payment):
#     def make_payment(self, amount):
#         return f"Payment of ${amount} made using PayPal."

# class CashPayment(Payment):
#     def make_payment(self, amount):
#         return f"Payment of ${amount} made using Cash."

# def main():
#     print("Choose your payment method:")
#     print("1. Credit Card")
#     print("2. PayPal")
#     print("3. Cash")
    
#     choice = input("Enter the number of your payment method (1-3): ")
    
#     try:
#         amount = float(input("Enter the amount to pay: $"))
#     except ValueError:
#         print("Invalid input! Amount must be a number.")
#         return

#     if choice == "1":
#         payment = CreditCardPayment()
#     elif choice == "2":
#         payment = PayPalPayment()
#     elif choice == "3":
#         payment = CashPayment()
#     else:
#         print("Invalid choice! Please select a valid payment method.")
#         return

#     print(payment.make_payment(amount))

# if __name__ == "_main_":
#     main()

# #overloading
# class OverloadExample:
#     def display(self, *args):
#         if len(args) == 0:
#             print("No arguments")
#         elif len(args) == 1:
#             print(f"One argument: {args[0]}")
#         elif len(args) == 2:
#             print(f"Two arguments: {args[0]}, {args[1]}")
#         else:
#             print("More than two arguments:", args)

# # Example Usage
# obj = OverloadExample()
# obj.display()               # Output: No arguments
# obj.display(10)             # Output: One argument: 10
# obj.display(10, 20)         # Output: Two arguments: 10, 20
# obj.display(1, 2, 3)        # Output: More than two arguments: (1, 2, 3)

# #overriding
# # Python program to demonstrate 
# # Defining parent class 
# class Parent(): 
    
#     # Constructor 
#     def __init__(self): 
#         self.value = "Inside Parent"
        
#     # Parent's show method 
#     def show(self): 
#         print(self.value) 
        
# # Defining child class 
# class Child(Parent): 
    
#     # Constructor 
#     def __init__(self): 
#         super().__init__()  # Call parent constructor
#         self.value = "Inside Child"
        
#     # Child's show method 
#     def show(self): 
#         print(self.value) 
        
# # Driver's code 
# obj1 = Parent() 
# obj2 = Child() 

# obj1.show()  # Should print "Inside Parent"
# obj2.show()  # Should print "Inside Child"

# #operator overloading
# # Python program to show use of
# # + operator for different purposes.

# print(1 + 2)

# # concatenate two strings
# print("KRUNALSINH "+"CHHASATIYA") 

# # Product two numbers
# print(3 * 4)

# # Repeat the String
# print("KRUNALSINH CHHASATIYA    "*4)

# Python Program illustrate how 
# to overload an binary + operator
# And how it actually works

# class A:
#     def __init__(self, a):
#         self.a = a

#     # adding two objects 
#     def __add__(self, o):
#         return self.a + o.a 
# ob1 = A(1)
# ob2 = A(2)
# ob3 = A("Krunalsinh ")
# ob4 = A("Chhasatiya")

# print(ob1 + ob2)
# print(ob3 + ob4)
# # Actual working when Binary Operator is used.
# print(A.__add__(ob1 , ob2)) 
# print(A.__add__(ob3,ob4)) 
# #And can also be Understand as :
# print(ob1.__add__(ob2))
# print(ob3.__add__(ob4))

#Enapsulation
# class Encap:
#     a = 10
#     _b = 30
#     __c = 20
#     def display(self):
#         print("WELCOME : PUBLIC METHOD")

#     def _display(self):
#         print("WELCOME : PROTECTED METHOD")
    
#     def __display(self):
#         print("WELCOME : PRIVATE METHOD")
# obj = Encap()
# print(obj.a)
# obj.display()
# obj._display()
# obj._Encap__display()
    
# # Public and Private Data Member
# class ABC:
#     def __init__(self, var1, var2):
#         self.var1 = var1
#         self.__var2 = var2
#     def display(self):
#         print(self.var1)
#         print(self.__var2)
# obj = ABC(10, 20)
# obj.display()
# print(obj.var1)
# print(obj._ABC__var2)

# Distructor
# class ABC:
#     class_var = 0
#     def __init__(self, var):
#         ABC.class_var += 1
#         self.var = var
#         print("THE OBJECT VALUE IS", var)
#         print("THE VALUE OF THE CLASS VARIABLE IS : ",ABC.class_var)
#     def __del__(self):
#         ABC.class_var -= 1
#         print("OBJECT WITH THE VALUE %d IS GOING OUT OF SCOPE "%self.var)
# obj1 = ABC(10)
# obj2 = ABC(20)
# obj3 = ABC(30)
# del obj1
# del obj2
# del obj3

# Class Method
# class rectangle:
#     def __init__(self, ln ,br):
#         self.ln = ln
#         self.br = br
#     def area(self):
#         return self.ln*self.br
#     @classmethod
#     def square(cls, side):
#         return cls(side, side)
# s = rectangle.square(10)
# print("AREA = ",s.area())

# Staic Method
class choice:
    def __init__(self,subjects):
        self.subjects = subjects
    @staticmethod
    def validate_subject(subjects):
        if "CSA" in subjects:
            print("THIS OPTION IS NO LONGER AVAILABLE")
        else:
            return True
subject = ["DS","CSA","OS","TOC"]
if all (choice.validate_subject(i) for i in subject):
    ch = choice(subject)
    print("YOU HAVE BEEN ALLOCATED SUBJECT : ",subject)