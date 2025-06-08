#1
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

#2
def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
#3
class Example:
    class_var = "I am a class variable"

    def _init_(self, value):
        self.instance_var = value
#4
class PrivateExample:
    def _init_(self):
        self.__private_var = "Private"

    def get_private_var(self):
        return self.__private_var
#5
class Math:
    def square(self, number):
        return number ** 2
#6
a = Math()
b = Math()
print(a.square(2))  # 4
print(b.square(3))  # 9

#7
class Student:
    def set_details(self, name, roll):
        self.name = name
        self.roll = roll

#8
print(isinstance(a, Math))  # True

#9
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

#10
class A:
    def method_A(self):
        print("Method A")

class B(A):
    def method_B(self):
        print("Method B")

class C(B):
    def method_C(self):
        print("Method C")

#11
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        print("Child class")

#12
class Parent2:
    def show(self):
        print("Parent method")

class Child2(Parent2):
    def show(self):
        super().show()
        print("Child method")

#13
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

#14
class Father:
    def father_method(self):
        print("Father method")

class Mother:
    def mother_method(self):
        print("Mother method")

class Child3(Father, Mother):
    pass

#15
class Encapsulation:
    def _init_(self):
        self.__value = 0

    def set_value(self, val):
        self.__value = val

    def get_value(self):
        return self.__value

#16
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()

#17
class Employee:
    count = 0

    def _init_(self):
        Employee.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total Employees: {cls.count}")

#18
class Overload:
    def _init_(self, a=0, b=0):
        self.sum = a + b

#19
class BankAccount:
    def _init_(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

#20
class Rectangle:
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)