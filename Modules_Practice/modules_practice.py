# ============================================================
# PYTHON MODULES & PACKAGES
# 20 QUESTIONS - BEGINNER TO ADVANCED
# ============================================================


# ============================================================
# Q1. Import the math module
# Use the math module to find the square root of 25.
# ============================================================

import math

result = math.sqrt(25)

print("Square root:", result)


# ============================================================
# Q2. Use math.pi
# Calculate the area of a circle.
#
# Formula:
# area = pi * radius^2
# ============================================================

import math

radius = 5

area = math.pi * radius ** 2

print("Area:", area)


# ============================================================
# Q3. Use math functions
# Find:
# - 2^5 using pow()
# - absolute value of -20 using fabs()
# - ceiling of 4.2
# - floor of 4.8
# ============================================================

import math

print("Power:", math.pow(2, 5))
print("Absolute value:", math.fabs(-20))
print("Ceiling:", math.ceil(4.2))
print("Floor:", math.floor(4.8))


# ============================================================
# Q4. Import only specific functions
# Import sqrt and factorial from math.
# ============================================================

from math import sqrt, factorial

print("Square root:", sqrt(49))
print("Factorial:", factorial(5))


# ============================================================
# Q5. Import a module with an alias
# Import math as m.
# Use m.sqrt() and m.pi.
# ============================================================

import math as m

print("Square root:", m.sqrt(100))
print("PI:", m.pi)


# ============================================================
# Q6. Random number
# Import random and generate a random number
# between 1 and 10.
# ============================================================

import random

number = random.randint(1, 10)

print("Random number:", number)


# ============================================================
# Q7. Random choice
# Create a list of fruits.
# Randomly select one fruit.
# ============================================================

import random

fruits = ["apple", "banana", "mango", "orange", "grape"]

fruit = random.choice(fruits)

print("Random fruit:", fruit)


# ============================================================
# Q8. Random password
# Create a program that generates a random 6-digit number.
# ============================================================

import random

password = ""

for i in range(6):
    password += str(random.randint(0, 9))

print("Your OTP:", password)


# ============================================================
# Q9. Date and time
# Import datetime.
# Print today's date.
# ============================================================

from datetime import datetime

today = datetime.now()

print("Current date and time:", today)


# ============================================================
# Q10. Get only the date
# Print the current date in this format:
#
# YYYY-MM-DD
# ============================================================

from datetime import datetime

today = datetime.now()

print("Date:", today.strftime("%Y-%m-%d"))


# ============================================================
# Q11. Get current time
# Print the current time in this format:
#
# HH:MM:SS
# ============================================================

from datetime import datetime

current_time = datetime.now()

print("Time:", current_time.strftime("%H:%M:%S"))


# ============================================================
# Q12. Create your own module
#
# Create TWO files:
#
# calculator.py
# main.py
#
# In calculator.py create functions:
# add()
# subtract()
# multiply()
# divide()
#
# Then import them into main.py.
#
# ------------------------------------------------------------
# SOLUTION FOR calculator.py
# ------------------------------------------------------------
#
# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a / b
#
#
# ------------------------------------------------------------
# SOLUTION FOR main.py
# ------------------------------------------------------------
#
# import calculator
#
# print(calculator.add(10, 5))
# print(calculator.subtract(10, 5))
# print(calculator.multiply(10, 5))
# print(calculator.divide(10, 5))
# ============================================================


# ============================================================
# Q13. Import functions from your own module
#
# calculator.py:
#
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b
#
#
# main.py should import only these functions.
# ============================================================

# from calculator import add, multiply

# print(add(10, 20))
# print(multiply(10, 20))


# ============================================================
# Q14. Create a greeting module
#
# Create:
#
# greeting.py
#
# It should contain:
#
# def hello(name):
#     return "Hello " + name
#
# Then import it into main.py.
# ============================================================

# ---------------- greeting.py ----------------
#
# def hello(name):
#     return "Hello " + name
#
#
# ---------------- main.py ----------------
#
# import greeting
#
# print(greeting.hello("Ram"))


# ============================================================
# Q15. Create a student module
#
# Create a module called student.py.
#
# Add:
# name
# age
# marks
#
# Also create a function:
# show_student()
#
# Import the module into main.py.
# ============================================================

# ---------------- student.py ----------------
#
# name = "Ram"
# age = 20
# marks = 85
#
#
# def show_student():
#     print("Name:", name)
#     print("Age:", age)
#     print("Marks:", marks)
#
#
# ---------------- main.py ----------------
#
# import student
#
# student.show_student()


# ============================================================
# Q16. Use the os module
#
# Import os.
#
# Print:
# - current working directory
# - files and folders in the current directory
# ============================================================

import os

print("Current directory:")
print(os.getcwd())

print("\nFiles and folders:")
print(os.listdir())


# ============================================================
# Q17. Create a utility module
#
# Create:
#
# my_utils.py
#
# Add functions:
# - is_even()
# - is_odd()
# - square()
#
# Then import the module and test the functions.
# ============================================================

# ---------------- my_utils.py ----------------
#
# def is_even(number):
#     return number % 2 == 0
#
#
# def is_odd(number):
#     return number % 2 != 0
#
#
# def square(number):
#     return number ** 2
#
#
# ---------------- main.py ----------------
#
# import my_utils
#
# print(my_utils.is_even(10))
# print(my_utils.is_odd(7))
# print(my_utils.square(5))


# ============================================================
# Q18. Create a calculator package
#
# Create this folder structure:
#
# calculator/
#     __init__.py
#     basic.py
#     advanced.py
#
# basic.py:
# - add()
# - subtract()
#
# advanced.py:
# - power()
# - square_root()
#
# Then import the functions into main.py.
# ============================================================

# Folder structure:
#
# calculator/
#     __init__.py
#     basic.py
#     advanced.py
#
#
# ---------------- basic.py ----------------
#
# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# ---------------- advanced.py ----------------
#
# import math
#
#
# def power(a, b):
#     return a ** b
#
#
# def square_root(a):
#     return math.sqrt(a)
#
#
# ---------------- main.py ----------------
#
# from calculator.basic import add, subtract
# from calculator.advanced import power, square_root
#
# print(add(10, 5))
# print(subtract(10, 5))
# print(power(2, 3))
# print(square_root(25))


# ============================================================
# Q19. ADVANCED - Random password generator module
#
# Create a module called password_generator.py.
#
# Create a function:
#
# generate_password(length)
#
# The function should generate a random password containing
# letters and numbers.
#
# Import it into main.py.
# ============================================================

# ---------------- password_generator.py ----------------
#
# import random
# import string
#
#
# def generate_password(length):
#
#     characters = string.ascii_letters + string.digits
#
#     password = ""
#
#     for i in range(length):
#         password += random.choice(characters)
#
#     return password
#
#
# ---------------- main.py ----------------
#
# import password_generator
#
# password = password_generator.generate_password(10)
#
# print("Generated password:", password)


# ============================================================
# Q20. ADVANCED - Student Management Package
#
# Create this structure:
#
# student_app/
#     __init__.py
#     student.py
#     calculations.py
#     main.py
#
# student.py:
#     Create a Student class with:
#     name
#     marks
#
# calculations.py:
#     Create functions:
#     average()
#     highest()
#     lowest()
#
# main.py:
#     Import the modules.
#     Create students.
#     Calculate their average, highest and lowest marks.
#
# ============================================================

# ---------------- student.py ----------------
#
# class Student:
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#
# ---------------- calculations.py ----------------
#
# def average(marks):
#     return sum(marks) / len(marks)
#
#
# def highest(marks):
#     return max(marks)
#
#
# def lowest(marks):
#     return min(marks)
#
#
# ---------------- main.py ----------------
#
# from student import Student
# import calculations
#
#
# students = [
#     Student("Ram", 80),
#     Student("Sita", 90),
#     Student("Hari", 75)
# ]
#
# marks = []
#
# for student in students:
#     marks.append(student.marks)
#
# print("Average:", calculations.average(marks))
# print("Highest:", calculations.highest(marks))
# print("Lowest:", calculations.lowest(marks))