# ============================================================
# PYTHON FUNCTIONS - 30 PRACTICE QUESTIONS
# Beginner to Advanced
# ============================================================


# ============================================================
# 🟢 BEGINNER
# ============================================================

# 1. Create a simple function
# Create a function called greet() that prints "Hello, Python!".


# Solution:
def greet():
    print("Hello, Python!")

greet()


# ------------------------------------------------------------

# 2. Create a function that prints your name
# Create a function called my_name() that prints your name.


# Solution:
def my_name():
    print("My name is Ram")

my_name()


# ------------------------------------------------------------

# 3. Function with a parameter
# Create a function that accepts a name and prints:
# "Hello, <name>"


# Solution:
def greet_user(name):
    print("Hello", name)

greet_user("Ram")


# ------------------------------------------------------------

# 4. Function with two parameters
# Create a function that accepts two numbers and prints their sum.


# Solution:
def add(a, b):
    print(a + b)

add(10, 20)


# ------------------------------------------------------------

# 5. Subtract two numbers
# Create a function that accepts two numbers
# and prints their difference.


# Solution:
def subtract(a, b):
    print(a - b)

subtract(20, 10)


# ------------------------------------------------------------

# 6. Multiply two numbers
# Create a function that accepts two numbers
# and prints their multiplication.


# Solution:
def multiply(a, b):
    print(a * b)

multiply(5, 4)


# ------------------------------------------------------------

# 7. Check even or odd
# Create a function that accepts a number
# and prints whether it is even or odd.


# Solution:
def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(7)


# ------------------------------------------------------------

# 8. Check positive, negative, or zero
# Create a function that accepts a number
# and prints:
# Positive
# Negative
# Zero


# Solution:
def check_number(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

check_number(-5)


# ------------------------------------------------------------

# 9. Find the largest of two numbers
# Create a function that accepts two numbers
# and prints the largest number.


# Solution:
def largest(a, b):
    if a > b:
        print(a)
    else:
        print(b)

largest(20, 15)


# ------------------------------------------------------------

# 10. Multiplication table
# Create a function that accepts a number
# and prints its multiplication table from 1 to 10.


# Solution:
def multiplication_table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

multiplication_table(5)


# ============================================================
# 🟡 INTERMEDIATE
# ============================================================

# 11. Return a sum
# Create a function that accepts two numbers
# and RETURNS their sum.
#
# Example:
# result = add(10, 20)
# print(result)


# Solution:
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print(result)


# ------------------------------------------------------------

# 12. Return the square
# Create a function that accepts a number
# and returns its square.


# Solution:
def square(number):
    return number ** 2

print(square(5))


# ------------------------------------------------------------

# 13. Return the largest number
# Create a function that accepts two numbers
# and returns the largest.


# Solution:
def find_largest(a, b):
    if a > b:
        return a
    else:
        return b

print(find_largest(50, 30))


# ------------------------------------------------------------

# 14. Check voting eligibility
# Create a function that accepts age.
# Return "Can vote" if age is 18 or above.
# Otherwise return "Cannot vote".


# Solution:
def can_vote(age):
    if age >= 18:
        return "Can vote"
    else:
        return "Cannot vote"

print(can_vote(20))


# ------------------------------------------------------------

# 15. Calculate factorial
# Create a function that accepts a number
# and returns its factorial.
#
# Example:
# 5! = 120


# Solution:
def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

print(factorial(5))


# ------------------------------------------------------------

# 16. Count vowels
# Create a function that accepts a string
# and returns the number of vowels.


# Solution:
def count_vowels(text):
    count = 0

    for char in text:
        if char in "aeiou":
            count += 1

    return count

print(count_vowels("python programming"))


# ------------------------------------------------------------

# 17. Reverse a string
# Create a function that accepts a string
# and returns the reversed string.
#
# Do not use a built-in reverse function.


# Solution:
def reverse_string(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text

print(reverse_string("python"))


# ------------------------------------------------------------

# 18. Check palindrome
# Create a function that checks whether a word
# is a palindrome.
#
# Example:
# madam -> palindrome
# python -> not palindrome


# Solution:
def is_palindrome(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    if text == reversed_text:
        return True
    else:
        return False

print(is_palindrome("madam"))


# ------------------------------------------------------------

# 19. Sum of a list
# Create a function that accepts a list of numbers
# and returns the total.


# Solution:
def list_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

numbers = [10, 20, 30, 40]
print(list_sum(numbers))


# ------------------------------------------------------------

# 20. Find the largest number in a list
# Create a function that accepts a list
# and returns the largest number.
#
# Do not use max().


# Solution:
def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

numbers = [10, 50, 20, 80, 30]

print(find_max(numbers))


# ============================================================
# 🔴 ADVANCED
# ============================================================

# 21. Count even numbers in a list
# Create a function that accepts a list
# and returns how many even numbers it contains.


# Solution:
def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count

numbers = [1, 2, 3, 4, 5, 6]

print(count_even(numbers))


# ------------------------------------------------------------

# 22. Separate even and odd numbers
# Create a function that accepts a list
# and returns two lists:
#
# even numbers
# odd numbers


# Solution:
def separate_numbers(numbers):
    even = []
    odd = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    return even, odd

numbers = [1, 2, 3, 4, 5, 6]

even, odd = separate_numbers(numbers)

print("Even:", even)
print("Odd:", odd)


# ------------------------------------------------------------

# 23. Remove duplicates
# Create a function that accepts a list
# and returns a new list without duplicates.


# Solution:
def remove_duplicates(numbers):
    unique = []

    for number in numbers:
        if number not in unique:
            unique.append(number)

    return unique

numbers = [1, 2, 2, 3, 4, 4, 5]

print(remove_duplicates(numbers))


# ------------------------------------------------------------

# 24. Find the second largest number
# Create a function that accepts a list
# and returns the second largest number.


# Solution:
def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]

    for number in numbers:
        if number > largest:
            second = largest
            largest = number

        elif number > second and number != largest:
            second = number

    return second

numbers = [10, 50, 30, 80, 20]

print(second_largest(numbers))


# ------------------------------------------------------------

# 25. Prime number checker
# Create a function that accepts a number
# and returns True if it is prime.
# Otherwise return False.


# Solution:
def is_prime(number):

    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

print(is_prime(7))


# ------------------------------------------------------------

# 26. Find all prime numbers
# Create a function that accepts a number
# and returns a list of all prime numbers
# from 2 to that number.


# Solution:
def prime_numbers(limit):
    primes = []

    for number in range(2, limit + 1):

        is_prime_number = True

        for i in range(2, number):
            if number % i == 0:
                is_prime_number = False
                break

        if is_prime_number:
            primes.append(number)

    return primes

print(prime_numbers(50))


# ------------------------------------------------------------

# 27. Student grade function
# Create a function that accepts marks
# and returns:
#
# 90+  -> A
# 80+  -> B
# 70+  -> C
# 60+  -> D
# Below 60 -> F


# Solution:
def calculate_grade(marks):

    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print(calculate_grade(85))


# ------------------------------------------------------------

# 28. Student information function
# Create a function that accepts:
#
# name
# age
# marks
#
# The function should return a dictionary
# containing the student's information.


# Solution:
def student_info(name, age, marks):

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    return student

student = student_info("Ram", 20, 85)

print(student)


# ------------------------------------------------------------

# 29. Shopping cart function
# Create a function that accepts a dictionary
# containing products and prices.
#
# Example:
#
# products = {
#     "apple": 100,
#     "banana": 50,
#     "orange": 80
# }
#
# Calculate and return the total price.


# Solution:
def calculate_total(products):

    total = 0

    for price in products.values():
        total += price

    return total


products = {
    "apple": 100,
    "banana": 50,
    "orange": 80
}

print(calculate_total(products))


# ------------------------------------------------------------

# 30. 🔥 Mini Project - Calculator Function
#
# Create a function called calculator()
# that accepts:
#
# number1
# number2
# operator
#
# Operators:
#
# +  addition
# -  subtraction
# *  multiplication
# /  division
#
# Example:
#
# calculator(10, 5, "+")
# -> 15
#
# calculator(10, 5, "*")
# -> 50
#
# calculator(10, 5, "/")
# -> 2
#
# Handle division by zero.


# Solution:
def calculator(number1, number2, operator):

    if operator == "+":
        return number1 + number2

    elif operator == "-":
        return number1 - number2

    elif operator == "*":
        return number1 * number2

    elif operator == "/":

        if number2 == 0:
            return "Cannot divide by zero"

        return number1 / number2

    else:
        return "Invalid operator"


print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))