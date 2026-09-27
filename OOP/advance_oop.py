# ============================================================
# ADVANCED OOP
# 20 QUESTIONS - BEGINNER TO ADVANCED
# ============================================================


# ============================================================
# Q1. Basic inheritance
#
# Create a Person class with a name.
# Create a Student class that inherits Person.
# Print the student's name.
# ============================================================

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):
    pass


student = Student("Ram")

print(student.name)


# ============================================================
# Q2. Inheritance with multiple attributes
#
# Person:
# name
# age
#
# Student:
# student_id
#
# Use super() to initialize Person.
# ============================================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


student = Student("Sita", 20, 101)

print(student.name)
print(student.age)
print(student.student_id)


# ============================================================
# Q3. Add methods to parent and child
#
# Person has:
# introduce()
#
# Student has:
# study()
# ============================================================

class Person:

    def introduce(self):
        print("Hello, I am a person.")


class Student(Person):

    def study(self):
        print("I am studying.")


student = Student()

student.introduce()
student.study()


# ============================================================
# Q4. Method overriding
#
# Create Animal with speak().
#
# Dog should override speak().
# Cat should override speak().
# ============================================================

class Animal:

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def speak(self):
        print("Dog says Woof.")


class Cat(Animal):

    def speak(self):
        print("Cat says Meow.")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


# ============================================================
# Q5. Use super() with overridden method
#
# Parent class has show().
#
# Child class should call the parent's show()
# and then print its own message.
# ============================================================

class Parent:

    def show(self):
        print("This is the parent class.")


class Child(Parent):

    def show(self):
        super().show()
        print("This is the child class.")


child = Child()

child.show()


# ============================================================
# Q6. Create a Vehicle hierarchy
#
# Vehicle:
# brand
#
# Car:
# number_of_doors
#
# Bike:
# has_gears
# ============================================================

class Vehicle:

    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):

    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors


class Bike(Vehicle):

    def __init__(self, brand, gears):
        super().__init__(brand)
        self.gears = gears


car = Car("Toyota", 4)
bike = Bike("Yamaha", 5)

print(car.brand, car.doors)
print(bike.brand, bike.gears)


# ============================================================
# Q7. Polymorphism
#
# Create Dog, Cat and Cow.
# Each class should have speak().
#
# Store them in one list and call speak() in a loop.
# ============================================================

class Dog:

    def speak(self):
        print("Woof")


class Cat:

    def speak(self):
        print("Meow")


class Cow:

    def speak(self):
        print("Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()


# ============================================================
# Q8. Polymorphism with area()
#
# Create:
# Circle
# Rectangle
# Triangle
#
# Each class should have area().
# Put all objects in a list and calculate their areas.
# ============================================================

import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Rectangle(10, 5),
    Triangle(10, 4)
]

for shape in shapes:
    print("Area:", shape.area())


# ============================================================
# Q9. Encapsulation
#
# Create a BankAccount class.
#
# Make balance private:
# __balance
#
# Create:
# deposit()
# withdraw()
# get_balance()
# ============================================================

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal.")

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(1000)
account.withdraw(2000)

print("Balance:", account.get_balance())


# ============================================================
# Q10. Private method
#
# Create a User class.
#
# Create a private method:
# __validate_password()
#
# The login() method should use the private method.
# ============================================================

class User:

    def __init__(self, password):
        self.__password = password

    def __validate_password(self, password):

        return password == self.__password

    def login(self, password):

        if self.__validate_password(password):
            print("Login successful.")
        else:
            print("Wrong password.")


user = User("python123")

user.login("python123")
user.login("wrong")


# ============================================================
# Q11. Class method
#
# Create a Student class.
#
# Create a class variable:
# school = "ABC School"
#
# Create a class method called change_school()
# that changes the school name.
# ============================================================

class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


print(Student.school)

Student.change_school("XYZ School")

print(Student.school)


# ============================================================
# Q12. Static method
#
# Create a MathUtils class.
#
# Create static methods:
# add()
# multiply()
# square()
# ============================================================

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def square(a):
        return a ** 2


print(MathUtils.add(10, 5))
print(MathUtils.multiply(10, 5))
print(MathUtils.square(5))


# ============================================================
# Q13. Property
#
# Create a Person class.
#
# Store age privately:
# __age
#
# Use @property to get age.
#
# Use a setter to prevent negative age.
# ============================================================

class Person:

    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):

        if value < 0:
            raise ValueError("Age cannot be negative.")

        self.__age = value


person = Person(20)

print(person.age)

person.age = 25

print(person.age)


# ============================================================
# Q14. Multiple inheritance
#
# Create:
#
# Father
# Mother
# Child
#
# Child should inherit from both Father and Mother.
# ============================================================

class Father:

    def father_skill(self):
        print("Father can drive.")


class Mother:

    def mother_skill(self):
        print("Mother can cook.")


class Child(Father, Mother):

    def child_skill(self):
        print("Child can study.")


child = Child()

child.father_skill()
child.mother_skill()
child.child_skill()


# ============================================================
# Q15. Multiple inheritance with constructors
#
# Create:
# Father with father_name
# Mother with mother_name
#
# Child should inherit from both.
# ============================================================

class Father:

    def __init__(self, father_name):
        self.father_name = father_name


class Mother:

    def __init__(self, mother_name):
        self.mother_name = mother_name


class Child(Father, Mother):

    def __init__(self, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)


child = Child("Ram", "Sita")

print("Father:", child.father_name)
print("Mother:", child.mother_name)


# ============================================================
# Q16. Abstract class
#
# Create an abstract class Animal.
#
# It should contain an abstract method:
# speak()
#
# Create Dog and Cat classes that implement speak().
# ============================================================

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print("Woof")


class Cat(Animal):

    def speak(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


# ============================================================
# Q17. Abstract payment system
#
# Create an abstract Payment class.
#
# Methods:
# pay()
#
# Create:
# CreditCard
# PayPal
# Cash
#
# Each class should implement pay().
# ============================================================

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Credit Card.")


class PayPal(Payment):

    def pay(self, amount):
        print("Paid", amount, "using PayPal.")


class Cash(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Cash.")


payments = [
    CreditCard(),
    PayPal(),
    Cash()
]

for payment in payments:
    payment.pay(1000)


# ============================================================
# Q18. ADVANCED - Employee Management System
#
# Create:
#
# Employee
# Manager
# Developer
#
# Employee:
# name
# salary
#
# Manager:
# department
#
# Developer:
# programming_language
#
# Each class should have show_info().
#
# Use inheritance and method overriding.
# ============================================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        super().show_info()
        print("Department:", self.department)


class Developer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show_info(self):
        super().show_info()
        print("Programming Language:", self.language)


manager = Manager("Ram", 80000, "IT")
developer = Developer("Sita", 70000, "Python")

manager.show_info()

print()

developer.show_info()


# ============================================================
# Q19. ADVANCED - Library Management System
#
# Create:
#
# Book
# Member
# Library
#
# Book:
# title
# author
# available
#
# Member:
# name
#
# Library:
# books
# members
#
# Methods:
# add_book()
# add_member()
# borrow_book()
# return_book()
# ============================================================

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Member:

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, book):

        if book.available:

            book.available = False
            member.borrowed_books.append(book)

            print(member.name, "borrowed", book.title)

        else:

            print("Book is not available.")

    def return_book(self, member, book):

        if book in member.borrowed_books:

            book.available = True
            member.borrowed_books.remove(book)

            print(member.name, "returned", book.title)

        else:

            print("This member did not borrow this book.")


library = Library()

book1 = Book("Python Basics", "John")
book2 = Book("Learn OOP", "David")

member1 = Member("Ram")

library.add_book(book1)
library.add_book(book2)

library.add_member(member1)

library.borrow_book(member1, book1)

library.return_book(member1, book1)


# ============================================================
# Q20. ADVANCED - COMPLETE BANKING SYSTEM
#
# Create:
#
# Account
# SavingsAccount
# CurrentAccount
#
# Account:
# account_number
# owner
# balance
#
# Methods:
# deposit()
# withdraw()
# show_balance()
#
# SavingsAccount:
# withdraw() should prevent withdrawal if balance
# becomes less than 500.
#
# CurrentAccount:
# allow withdrawal as long as balance does not go
# below -1000.
#
# Use:
# inheritance
# encapsulation
# method overriding
# polymorphism
# ============================================================

class Account:

    def __init__(self, account_number, owner, balance):

        self.account_number = account_number
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit.")

        else:
            self._balance += amount
            print("Deposit successful.")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal.")

        elif amount > self._balance:
            print("Insufficient balance.")

        else:
            self._balance -= amount
            print("Withdrawal successful.")

    def show_balance(self):

        print(
            self.owner,
            "Balance:",
            self._balance
        )


class SavingsAccount(Account):

    def withdraw(self, amount):

        if amount <= 0:

            print("Invalid withdrawal.")

        elif self._balance - amount < 500:

            print(
                "Savings account must keep "
                "at least 500."
            )

        else:

            self._balance -= amount

            print(
                "Savings withdrawal successful."
            )


class CurrentAccount(Account):

    def withdraw(self, amount):

        if amount <= 0:

            print("Invalid withdrawal.")

        elif self._balance - amount < -1000:

            print(
                "Current account limit exceeded."
            )

        else:

            self._balance -= amount

            print(
                "Current account withdrawal successful."
            )


savings = SavingsAccount(
    101,
    "Ram",
    5000
)

current = CurrentAccount(
    102,
    "Sita",
    2000
)

savings.deposit(1000)
savings.withdraw(4000)
savings.show_balance()

print()

current.withdraw(2500)
current.show_balance()