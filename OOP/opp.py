# ============================================================
# PYTHON OOP - OBJECT ORIENTED PROGRAMMING
# 20 QUESTIONS - BEGINNER TO ADVANCED
# ============================================================


# ============================================================
# Q1. Create a simple class
#
# Create a class called Student.
# Create an object from the class.
# ============================================================

class Student:
    pass


student1 = Student()

print(student1)


# ============================================================
# Q2. Create a class with an attribute
#
# Create a Student class.
# Give the student a name.
# Print the name.
# ============================================================

class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Ram")

print(student1.name)


# ============================================================
# Q3. Create multiple attributes
#
# Create a Student class with:
# name
# age
# marks
#
# Print all three values.
# ============================================================

class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


student1 = Student("Ram", 20, 85)

print("Name:", student1.name)
print("Age:", student1.age)
print("Marks:", student1.marks)


# ============================================================
# Q4. Create multiple objects
#
# Create three Student objects with different information.
# Print their information.
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Ram", 20)
student2 = Student("Sita", 21)
student3 = Student("Hari", 19)

print(student1.name, student1.age)
print(student2.name, student2.age)
print(student3.name, student3.age)


# ============================================================
# Q5. Create a method
#
# Create a Student class.
# Create a method called introduce().
#
# It should print:
# "Hello, my name is Ram"
# ============================================================

class Student:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is", self.name)


student1 = Student("Ram")

student1.introduce()


# ============================================================
# Q6. Create a calculator class
#
# Create a Calculator class with methods:
#
# add()
# subtract()
# multiply()
# divide()
# ============================================================

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


calculator = Calculator()

print("Add:", calculator.add(10, 5))
print("Subtract:", calculator.subtract(10, 5))
print("Multiply:", calculator.multiply(10, 5))
print("Divide:", calculator.divide(10, 5))


# ============================================================
# Q7. Create a Car class
#
# Attributes:
# brand
# model
# year
#
# Method:
# display_info()
# ============================================================

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


car1 = Car("Toyota", "Corolla", 2024)

car1.display_info()


# ============================================================
# Q8. Bank Account
#
# Create a BankAccount class.
#
# Attributes:
# account_holder
# balance
#
# Methods:
# deposit()
# withdraw()
# show_balance()
# ============================================================

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print("Balance:", self.balance)


account = BankAccount("Ram", 5000)

account.deposit(2000)
account.withdraw(1000)

account.show_balance()


# ============================================================
# Q9. Rectangle class
#
# Create a Rectangle class.
#
# Attributes:
# length
# width
#
# Methods:
# area()
# perimeter()
# ============================================================

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(10, 5)

print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())


# ============================================================
# Q10. Employee class
#
# Create an Employee class with:
#
# name
# salary
#
# Create a method:
# show_salary()
#
# Create two employees.
# ============================================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        print(self.name, "earns", self.salary)


employee1 = Employee("Ram", 50000)
employee2 = Employee("Sita", 60000)

employee1.show_salary()
employee2.show_salary()


# ============================================================
# Q11. Class variable
#
# Create a Student class.
#
# Create a class variable:
#
# school = "ABC School"
#
# Create two students and print their school.
# ============================================================

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name


student1 = Student("Ram")
student2 = Student("Sita")

print(student1.name, student1.school)
print(student2.name, student2.school)


# ============================================================
# Q12. Count objects
#
# Create a Student class.
# Use a class variable to count how many Student objects
# have been created.
# ============================================================

class Student:

    student_count = 0

    def __init__(self, name):

        self.name = name

        Student.student_count += 1


student1 = Student("Ram")
student2 = Student("Sita")
student3 = Student("Hari")

print("Total students:", Student.student_count)


# ============================================================
# Q13. Student grade system
#
# Create a Student class.
#
# Attributes:
# name
# marks
#
# Create a method:
# get_grade()
#
# Rules:
#
# 90+ = A
# 80+ = B
# 70+ = C
# 60+ = D
# below 60 = F
# ============================================================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 80:
            return "B"

        elif self.marks >= 70:
            return "C"

        elif self.marks >= 60:
            return "D"

        else:
            return "F"


student = Student("Ram", 85)

print("Name:", student.name)
print("Grade:", student.get_grade())


# ============================================================
# Q14. Encapsulation
#
# Create a BankAccount class.
#
# Make balance a private attribute using:
#
# __balance
#
# Create methods:
# deposit()
# withdraw()
# get_balance()
# ============================================================

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(1000)
account.withdraw(2000)

print("Balance:", account.get_balance())


# ============================================================
# Q15. Inheritance
#
# Create:
#
# Parent class: Animal
# Method: speak()
#
# Child class: Dog
# Method: bark()
#
# Dog should inherit from Animal.
# ============================================================

class Animal:

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def bark(self):
        print("Dog barks.")


dog = Dog()

dog.speak()
dog.bark()


# ============================================================
# Q16. Inheritance with attributes
#
# Create a Person class with:
# name
# age
#
# Create a Student class that inherits Person.
#
# Student should also have:
# student_id
# ============================================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, student_id):

        super().__init__(name, age)

        self.student_id = student_id


student = Student("Ram", 20, 101)

print("Name:", student.name)
print("Age:", student.age)
print("ID:", student.student_id)


# ============================================================
# Q17. Method overriding
#
# Create:
#
# Animal
# Dog
# Cat
#
# Each class should have a speak() method.
#
# Dog should print "Woof"
# Cat should print "Meow"
# ============================================================

class Animal:

    def speak(self):
        print("Animal sound")


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
# Q18. Polymorphism
#
# Create Dog and Cat classes.
#
# Both should have speak().
#
# Put objects inside a list and loop through them.
# ============================================================

class Dog:

    def speak(self):
        print("Dog says Woof")


class Cat:

    def speak(self):
        print("Cat says Meow")


class Cow:

    def speak(self):
        print("Cow says Moo")


animals = [
    Dog(),
    Cat(),
    Cow()
]

for animal in animals:
    animal.speak()


# ============================================================
# Q19. ADVANCED - Library Management System
#
# Create a Book class:
#
# title
# author
# available
#
# Methods:
# borrow_book()
# return_book()
# show_info()
#
# A user should only be able to borrow a book if it
# is available.
# ============================================================

class Book:

    def __init__(self, title, author):

        self.title = title
        self.author = author
        self.available = True

    def borrow_book(self):

        if self.available:
            self.available = False
            print("Book borrowed successfully.")

        else:
            print("Book is already borrowed.")

    def return_book(self):

        if not self.available:
            self.available = True
            print("Book returned successfully.")

        else:
            print("Book was not borrowed.")

    def show_info(self):

        print("Title:", self.title)
        print("Author:", self.author)

        if self.available:
            print("Status: Available")
        else:
            print("Status: Borrowed")


book = Book("Python Basics", "John Smith")

book.show_info()

book.borrow_book()

book.show_info()

book.return_book()

book.show_info()


# ============================================================
# Q20. ADVANCED - ATM OOP PROJECT
#
# Create an ATM class.
#
# Attributes:
# account_holder
# balance
#
# Methods:
# check_balance()
# deposit()
# withdraw()
# show_account()
#
# Requirements:
#
# 1. Deposit money.
# 2. Withdraw money.
# 3. Do not allow negative deposits.
# 4. Do not allow withdrawal greater than balance.
# 5. Show account information.
# ============================================================

class ATM:

    def __init__(self, account_holder, balance):

        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):

        print("Current balance:", self.balance)

    def deposit(self, amount):

        if amount <= 0:
            print("Deposit must be greater than zero.")
        else:
            self.balance += amount
            print("Deposit successful.")

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal must be greater than zero.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def show_account(self):

        print("\n===== ACCOUNT =====")
        print("Account holder:", self.account_holder)
        print("Balance:", self.balance)


account = ATM("Ram", 10000)

account.show_account()

account.deposit(5000)

account.check_balance()

account.withdraw(3000)

account.check_balance()

account.withdraw(20000)

account.show_account()