# ============================================================
# PYTHON TUPLES - 30 PRACTICE QUESTIONS
# BEGINNER TO ADVANCED
# ============================================================


# ============================================================
# 🟢 BEGINNER
# ============================================================

# 1. Create a tuple
# Create a tuple containing:
# "apple", "banana", "mango"
#
# Print the tuple.


# Solution:
fruits = ("apple", "banana", "mango")

print(fruits)


# ------------------------------------------------------------
# 2. Access the first item
# Print the first item from:
#
# fruits = ("apple", "banana", "mango")


# Solution:
fruits = ("apple", "banana", "mango")

print(fruits[0])


# ------------------------------------------------------------
# 3. Access the last item
# Print the last item using negative indexing.


# Solution:
fruits = ("apple", "banana", "mango")

print(fruits[-1])


# ------------------------------------------------------------
# 4. Access the second item
# Print "banana" from the tuple.


# Solution:
fruits = ("apple", "banana", "mango")

print(fruits[1])


# ------------------------------------------------------------
# 5. Find the length
# Find how many items are inside:
#
# numbers = (10, 20, 30, 40, 50)


# Solution:
numbers = (10, 20, 30, 40, 50)

print(len(numbers))


# ------------------------------------------------------------
# 6. Check the data type
# Print the type of:
#
# numbers = (10, 20, 30)


# Solution:
numbers = (10, 20, 30)

print(type(numbers))


# ------------------------------------------------------------
# 7. Loop through a tuple
# Print every item:
#
# fruits = ("apple", "banana", "mango")


# Solution:
fruits = ("apple", "banana", "mango")

for fruit in fruits:
    print(fruit)


# ------------------------------------------------------------
# 8. Check if an item exists
# Check whether "mango" exists in:
#
# fruits = ("apple", "banana", "mango")


# Solution:
fruits = ("apple", "banana", "mango")

if "mango" in fruits:
    print("Mango exists")
else:
    print("Mango does not exist")


# ------------------------------------------------------------
# 9. Count an item
# Count how many times 5 appears:
#
# numbers = (5, 2, 5, 8, 5, 10)


# Solution:
numbers = (5, 2, 5, 8, 5, 10)

print(numbers.count(5))


# ------------------------------------------------------------
# 10. Find the position
# Find the index of "mango":
#
# fruits = ("apple", "banana", "mango")


# Solution:
fruits = ("apple", "banana", "mango")

print(fruits.index("mango"))


# ============================================================
# 🟡 INTERMEDIATE
# ============================================================

# 11. Tuple slicing
# Print the first three items:
#
# numbers = (10, 20, 30, 40, 50)


# Solution:
numbers = (10, 20, 30, 40, 50)

print(numbers[0:3])


# ------------------------------------------------------------
# 12. Print the last three items
#
# numbers = (10, 20, 30, 40, 50)


# Solution:
numbers = (10, 20, 30, 40, 50)

print(numbers[-3:])


# ------------------------------------------------------------
# 13. Reverse a tuple
# Reverse:
#
# numbers = (1, 2, 3, 4, 5)


# Solution:
numbers = (1, 2, 3, 4, 5)

reversed_numbers = numbers[::-1]

print(reversed_numbers)


# ------------------------------------------------------------
# 14. Convert list to tuple
# Convert:
#
# fruits = ["apple", "banana", "mango"]
#
# into a tuple.


# Solution:
fruits = ["apple", "banana", "mango"]

fruits_tuple = tuple(fruits)

print(fruits_tuple)


# ------------------------------------------------------------
# 15. Convert tuple to list
# Convert:
#
# numbers = (10, 20, 30, 40)
#
# into a list.


# Solution:
numbers = (10, 20, 30, 40)

numbers_list = list(numbers)

print(numbers_list)


# ------------------------------------------------------------
# 16. Add an item to a tuple
# Tuples cannot be changed directly.
#
# Add "orange" to:
#
# fruits = ("apple", "banana", "mango")
#
# by converting it to a list first.


# Solution:
fruits = ("apple", "banana", "mango")

fruits_list = list(fruits)

fruits_list.append("orange")

fruits = tuple(fruits_list)

print(fruits)


# ------------------------------------------------------------
# 17. Remove an item from a tuple
# Remove "banana" from:
#
# fruits = ("apple", "banana", "mango")
#
# by converting it to a list.


# Solution:
fruits = ("apple", "banana", "mango")

fruits_list = list(fruits)

fruits_list.remove("banana")

fruits = tuple(fruits_list)

print(fruits)


# ------------------------------------------------------------
# 18. Find the sum
# Find the sum of:
#
# numbers = (10, 20, 30, 40, 50)
#
# Do not use sum().


# Solution:
numbers = (10, 20, 30, 40, 50)

total = 0

for number in numbers:
    total += number

print(total)


# ------------------------------------------------------------
# 19. Find the largest number
# Find the largest number without using max():
#
# numbers = (10, 50, 20, 80, 30)


# Solution:
numbers = (10, 50, 20, 80, 30)

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)


# ------------------------------------------------------------
# 20. Find the smallest number
# Find the smallest number without using min():
#
# numbers = (10, 50, 20, 80, 30)


# Solution:
numbers = (10, 50, 20, 80, 30)

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(smallest)


# ============================================================
# 🔴 ADVANCED
# ============================================================

# 21. Tuple unpacking
# Given:
#
# person = ("Ram", 20, "Nepal")
#
# Store the values in:
# name
# age
# country
#
# Then print them.


# Solution:
person = ("Ram", 20, "Nepal")

name, age, country = person

print(name)
print(age)
print(country)


# ------------------------------------------------------------
# 22. Multiple assignment
# Swap two variables using tuple unpacking.
#
# a = 10
# b = 20
#
# Expected:
# a = 20
# b = 10


# Solution:
a = 10
b = 20

a, b = b, a

print("a:", a)
print("b:", b)


# ------------------------------------------------------------
# 23. Tuple with different data types
# Create a tuple containing:
#
# name = "Ram"
# age = 20
# height = 5.8
# student = True
#
# Print every item using a loop.


# Solution:
person = ("Ram", 20, 5.8, True)

for item in person:
    print(item)


# ------------------------------------------------------------
# 24. Find even numbers
# Given:
#
# numbers = (1, 2, 3, 4, 5, 6, 7, 8)
#
# Create a new tuple containing only even numbers.


# Solution:
numbers = (1, 2, 3, 4, 5, 6, 7, 8)

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

even_numbers = tuple(even_numbers)

print(even_numbers)


# ------------------------------------------------------------
# 25. Remove duplicates
# Given:
#
# numbers = (1, 2, 2, 3, 4, 4, 5)
#
# Create a new tuple without duplicates.
#
# Do not use set().


# Solution:
numbers = (1, 2, 2, 3, 4, 4, 5)

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

unique = tuple(unique)

print(unique)


# ------------------------------------------------------------
# 26. Nested tuple
# Given:
#
# students = (
#     ("Ram", 20),
#     ("Sita", 21),
#     ("Hari", 19)
# )
#
# Print each student's name and age.


# Solution:
students = (
    ("Ram", 20),
    ("Sita", 21),
    ("Hari", 19)
)

for name, age in students:
    print("Name:", name)
    print("Age:", age)


# ------------------------------------------------------------
# 27. Find the oldest student
# Given:
#
# students = (
#     ("Ram", 20),
#     ("Sita", 25),
#     ("Hari", 19),
#     ("Gita", 22)
# )
#
# Find and print the oldest student's name and age.


# Solution:
students = (
    ("Ram", 20),
    ("Sita", 25),
    ("Hari", 19),
    ("Gita", 22)
)

oldest_name = ""
oldest_age = 0

for name, age in students:
    if age > oldest_age:
        oldest_age = age
        oldest_name = name

print("Oldest:", oldest_name)
print("Age:", oldest_age)


# ------------------------------------------------------------
# 28. Function returning a tuple
# Create a function called calculate()
# that accepts two numbers.
#
# It should return:
# addition
# subtraction
# multiplication
#
# as a tuple.


# Solution:
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(10, 5)

print(result)


# ------------------------------------------------------------
# 29. Student information
# Create a function that accepts:
#
# name
# age
# marks
#
# Return all three values as a tuple.
#
# Then unpack the returned tuple.


# Solution:
def student_info(name, age, marks):
    return name, age, marks


student = student_info("Ram", 20, 85)

name, age, marks = student

print("Name:", name)
print("Age:", age)
print("Marks:", marks)


# ------------------------------------------------------------
# 30. 🔥 ADVANCED CHALLENGE
#
# Create a student management program using tuples.
#
# Store students like:
#
# students = (
#     ("Ram", 80),
#     ("Sita", 95),
#     ("Hari", 70),
#     ("Gita", 85)
# )
#
# Your program should:
#
# 1. Print all students
# 2. Find the highest mark
# 3. Find the lowest mark
# 4. Calculate the average
# 5. Count students who passed
#
# A student passes if marks >= 40.


# Solution:
students = (
    ("Ram", 80),
    ("Sita", 95),
    ("Hari", 70),
    ("Gita", 85)
)

total = 0
highest = students[0]
lowest = students[0]
passed = 0

print("Students:")

for name, marks in students:
    print(name, marks)

    total += marks

    if marks > highest[1]:
        highest = (name, marks)

    if marks < lowest[1]:
        lowest = (name, marks)

    if marks >= 40:
        passed += 1

average = total / len(students)

print()
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Passed:", passed)