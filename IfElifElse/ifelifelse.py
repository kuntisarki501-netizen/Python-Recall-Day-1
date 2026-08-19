# Python if, elif, else: Practice Questions

# 1. Basic if

# Question:
# Write a program that prints "You are an adult" if age is 18 or older.

age = 20
if age >= 18:
    print("You are an adult")


# 2. if and else

# Question:
# Check whether a number is positive or not positive.

num = 5

if num > 0:
    print("Positive")
else:
    print("Not positive")    



age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are not adult")    


# 3. Check even or odd

# Question:
# Write a program to determine whether a number is even or odd.

num = 8
if num % 2== 0:
    print("Number is even")
else:
    print("Number is odd")


# 4. Check whether someone can vote

# Question:
# A person can vote if they are at least 18 years old.

age = 20

if age >= 18:
    print("You can vote.")
else:
    print("You can't vote")



# 5. Using elif

# Question:
# Print a student's grade based on their marks:

# 90–100 → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# Below 60 → F

marks = 85
if marks >= 90:
    print("A")
elif marks >=80:
    print("B")
elif marks >=70:
    print("C")
elif marks >=60:
    print("D")
else:
    print("F")    




# 6. Find the largest of two numbers

# Question:
# Find which of two numbers is larger.

a = 25
b = 20


if a > b :
    print(" a is larger")

elif b > a:
    print("b is larger")    
else:
    print("both are equal")



# 7. Find the largest of three numbers

# Question:
# Find the largest among three numbers.

a = 5
b = 10
c = 15

if a >= b and a >=c:
    print("a is largest ")
elif b >= a and b >=c:
    print("b is largest")
else:
    print("c is largest")    


# 8. Multiple conditions

# Question:
# A student passes if their marks are at least 40 and their attendance is at least 75%.    

mark = 40
attendance = 75
if mark >= 40 and  attendance >= 75:
    print("Pass")
else:
    print("Fail")


# 9. Nested if

# Question:
# Check whether a person is old enough to enter a club. If they are 18 or older, also check whether they have an ID.

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("You need an ID")
else:
    print("Yor are too young for club to entry")       


# Challenge Level
# 10. Login system

# Question:
# Create a simple login system. The username must be "admin" and the password must be "1234".   

user_name = "admin"
password = "1234"

if user_name == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")



# 11. Number classification

# Question:
# Determine whether a number is:

# Positive
# Negative
# Zero    

num = -1

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")       


# 12. Leap year

# Question:
# Write a program that determines whether a year is a leap year.

# A year is a leap year if:

# it is divisible by 400, or
# it is divisible by 4 but not by 100.

year = 2024

if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not a leap year")


# Advanced
# 13. Discount calculator

# Question:
# A store gives discounts based on the purchase amount:

# ₹10,000 or more → 20%
# ₹5,000–₹9,999 → 10%
# Below ₹5,000 → no discount

price = 7500
if price >= 10000:
    discount = 0.20
elif price >= 5000:
    discount = 0.10
else:
    discount = 0

final_price = price - (price * discount)

print(final_price)            


# 14. Login with multiple conditions

# Question:
# Allow login only if:

# username is correct,
# password is correct,
# account is active.

username = "Kunti"
password = "12345"
account_active = True

if username == "Kunti" and password =="12345":
    if account_active:
        print("Login Successful")
    else:
        print("Account is in active")

else:
    print("Invalid credentials")



# 15. Nested conditions with age

# Question:
# Classify a person:

# Under 13 → Child
# 13–19 → Teenager
# 20–59 → Adult
# 60+ → Senior

# Also, if the person is an adult, determine whether they are a working-age adult (20–59).

age = 35

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
    print("Working-age adult")
else:
    print("Senior")


# Advanced Challenge: Predict the Output

# Try these before looking at the answer.

# 16. What will this print?

x = 10

if x > 5:
    print("A")
elif x > 8:
    print("B")
else:
    print("C")



x = 5

if x > 10:
    print("A")
if x > 3:
    print("B")
else:
    print("C")


# Master Challenge
# 19. ATM withdrawal

# Write a program that checks whether a person can withdraw money.

# Rules:

# The PIN must be correct.
# The withdrawal amount must be greater than 0.
# The amount cannot exceed the account balance.
# If everything is valid, subtract the amount from the balance.

correct_pin = 1234
entered_pin = 1234
balance = 5000
amount = 2000

if entered_pin == correct_pin:
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance = balance - amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)
else:
    print("Incorrect PIN")



# Final Challenge: Build a Grade System
# 20. Question

# Create a program that accepts a student's marks and prints:

# A for 90+
# B for 80–89
# C for 70–79
# D for 60–69
# F below 60

# But also reject marks below 0 or above 100.


marks = 85

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")