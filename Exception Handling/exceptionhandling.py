# ============================================================
# PYTHON EXCEPTION HANDLING
# 20 QUESTIONS - BEGINNER TO ADVANCED
# ============================================================


# ============================================================
# Q1. Basic try-except
# Ask the user to enter a number.
# Handle the error if they enter something that is not a number.
# ============================================================

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Please enter a valid number.")


# ============================================================
# Q2. Division by zero
# Ask the user for two numbers and divide them.
# Handle division by zero.
# ============================================================

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("You cannot divide by zero.")


# ============================================================
# Q3. Handle multiple errors
# Ask for two integers and divide them.
# Handle both invalid input and division by zero.
# ============================================================

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ValueError:
    print("Please enter integers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ============================================================
# Q4. try-except-else
# If the user enters a valid number, print "Success".
# Otherwise print an error.
# ============================================================

try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("Success!")
    print("Your number is:", num)


# ============================================================
# Q5. try-except-finally
# Ask the user for a number.
# Use finally to print "Program finished".
# ============================================================

try:
    num = int(input("Enter a number: "))
    print("Number:", num)

except ValueError:
    print("Invalid input.")

finally:
    print("Program finished.")


# ============================================================
# Q6. List index error
# Create a list of 5 items.
# Ask the user for an index.
# Handle IndexError.
# ============================================================

fruits = ["apple", "banana", "orange", "mango", "grape"]

try:
    index = int(input("Enter an index: "))
    print("Fruit:", fruits[index])

except IndexError:
    print("That index does not exist.")

except ValueError:
    print("Please enter a number.")


# ============================================================
# Q7. Dictionary KeyError
# Create a dictionary of students and marks.
# Ask the user for a student name.
# Handle KeyError if the student doesn't exist.
# ============================================================

students = {
    "Ram": 80,
    "Sita": 90,
    "Hari": 75
}

try:
    name = input("Enter student name: ")
    print("Marks:", students[name])

except KeyError:
    print("Student not found.")


# ============================================================
# Q8. FileNotFoundError
# Try to open a file that may not exist.
# Handle FileNotFoundError.
# ============================================================

try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("File does not exist.")


# ============================================================
# Q9. Safe integer input
# Create a program that keeps asking for a number
# until the user enters a valid integer.
# ============================================================

while True:
    try:
        num = int(input("Enter an integer: "))
        print("Valid number:", num)
        break

    except ValueError:
        print("Invalid input. Try again.")


# ============================================================
# Q10. Safe division function
# Create a function called safe_divide().
# It should handle invalid numbers and division by zero.
# ============================================================

def safe_divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero."

    except TypeError:
        return "Invalid data type."


print(safe_divide(10, 2))
print(safe_divide(10, 0))


# ============================================================
# Q11. Age validation
# Ask the user for their age.
# Handle:
# - non-numbers
# - negative age
# - age greater than 120
# ============================================================

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age > 120:
        raise ValueError("Age cannot be greater than 120.")

    print("Your age is:", age)

except ValueError as error:
    print("Error:", error)


# ============================================================
# Q12. Password validation
# Ask the user for a password.
# Raise an exception if:
# - password is less than 8 characters
# ============================================================

try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")

    print("Password accepted.")

except ValueError as error:
    print("Error:", error)


# ============================================================
# Q13. Positive number validation
# Create a function that accepts only positive numbers.
# Use raise to create your own error.
# ============================================================

def check_positive(number):

    if number <= 0:
        raise ValueError("Number must be positive.")

    return number


try:
    num = int(input("Enter a positive number: "))
    print(check_positive(num))

except ValueError as error:
    print("Error:", error)


# ============================================================
# Q14. Simple calculator with exception handling
# Create a calculator that supports:
# +, -, *, /
#
# Handle:
# - invalid numbers
# - invalid operator
# - division by zero
# ============================================================

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2

    else:
        raise ValueError("Invalid operator.")

    print("Result:", result)

except ValueError as error:
    print("Error:", error)

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ============================================================
# Q15. File handling with exception handling
# Ask the user for a filename.
# Try to read the file.
# Handle FileNotFoundError.
# ============================================================

filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("The file was not found.")

except PermissionError:
    print("You do not have permission to open this file.")


# ============================================================
# Q16. Shopping program
# Create a dictionary containing product prices.
# Ask the user for a product.
# Ask for quantity.
#
# Handle:
# - product not found
# - invalid quantity
# ============================================================

products = {
    "apple": 50,
    "banana": 30,
    "milk": 80,
    "bread": 60
}

try:
    product = input("Enter product: ").lower()
    quantity = int(input("Enter quantity: "))

    price = products[product]

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    total = price * quantity

    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)

except KeyError:
    print("Product not found.")

except ValueError as error:
    print("Error:", error)


# ============================================================
# Q17. Student marks system
# Create a function that accepts marks.
#
# Rules:
# 0 <= marks <= 100
#
# Raise an exception if marks are outside this range.
# ============================================================

def check_marks(marks):

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    return marks


try:
    marks = float(input("Enter marks: "))
    check_marks(marks)
    print("Valid marks:", marks)

except ValueError as error:
    print("Error:", error)


# ============================================================
# Q18. Bank withdrawal system
#
# Create a balance variable.
# Ask the user how much they want to withdraw.
#
# Raise errors if:
# - withdrawal is negative
# - withdrawal is greater than balance
# - withdrawal is zero
# ============================================================

balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Withdrawal must be greater than zero.")

    if amount > balance:
        raise ValueError("Insufficient balance.")

    balance -= amount

    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except ValueError as error:
    print("Error:", error)


# ============================================================
# Q19. Login system with exception handling
#
# Create username and password.
# Ask the user to log in.
#
# Raise an exception if:
# - username is wrong
# - password is wrong
#
# Use try-except-finally.
# ============================================================

correct_username = "admin"
correct_password = "12345"

try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != correct_username:
        raise ValueError("Invalid username.")

    if password != correct_password:
        raise ValueError("Invalid password.")

    print("Login successful!")

except ValueError as error:
    print("Login failed:", error)

finally:
    print("Login process finished.")


# ============================================================
# Q20. ADVANCED - ATM SYSTEM
#
# Create a simple ATM program.
#
# Starting balance = 10000
#
# Menu:
# 1. Check balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
#
# Handle:
# - invalid menu choice
# - invalid numbers
# - negative deposit
# - negative withdrawal
# - insufficient balance
# - division/errors where appropriate
# ============================================================

balance = 10000

while True:

    print("\n===== ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:

            print("Your balance is:", balance)

        elif choice == 2:

            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                raise ValueError("Deposit must be greater than zero.")

            balance += amount

            print("Deposit successful.")
            print("New balance:", balance)

        elif choice == 3:

            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                raise ValueError(
                    "Withdrawal must be greater than zero."
                )

            if amount > balance:
                raise ValueError(
                    "Insufficient balance."
                )

            balance -= amount

            print("Withdrawal successful.")
            print("Remaining balance:", balance)

        elif choice == 4:

            print("Thank you for using the ATM.")
            break

        else:

            raise ValueError("Invalid menu choice.")

    except ValueError as error:

        print("Error:", error)

    finally:

        print("Transaction completed.")