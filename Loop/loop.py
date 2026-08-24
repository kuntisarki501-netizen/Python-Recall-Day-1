# Level 1 — Beginner (1–10)

# 1. Print numbers 1 to 10

# Write a for loop that prints numbers from 1 to 10.

for i in range(1, 11):
    print(i)


for i in range(1, 21):
    print(i)

# 3. Print even numbers

# Print all even numbers from 2 to 20.   

for i in range(2, 21, 2):
    print(i) 


for i in range(1, 21, 2):
    print(i)  



# 5. Print "Hello" 5 times

# Use a loop to print "Hello" five times.  

for i in range(5):
    print("Hello")


# 6 . Print a person's name 10 times
# name = "Ram"

# Print the name 10 times.


name = "Ram"

for i in range(10):
    print(name)



# 7. Countdown

# Print numbers from 10 down to 1. 

for i in range(10, 0, -1):
    print(i)



# 8. Print multiples of 5

for i in range(5, 51, 5):
    print(i)


#  9. Sum numbers from 1 to 10   

total = 0
for i in range(1, 11):
   total = total + i

   print(total)


# 10. Multiplication table

# Print the multiplication table of 5.   

num = 5

for i in range(1,11):
    print(num, "x", i, "=", num * i)


num = 2
for i in range(1, 11):
    print(num, "x", i, "=", num * i)    


    

# Level 2 — Beginner/Intermediate (11–20)

# 11. User-controlled multiplication table

# Ask the user for a number and print its multiplication table from 1 to 10.

user = int(input("enter the number="))

for i in range(1, 11):
    print(user, "x", i, "=", user * i)


# 12. Sum of even numbers

# Find the sum of all even numbers from 1 to 100.

total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total += i

print(total)


# 13. Count even numbers

# Count how many even numbers exist between 1 and 100.

count = 0

for i in range(1, 100):
    if i % 2 == 0:
        count +=1
print(count)        


# 14. Print numbers divisible by 3

# Print numbers between 1 and 50 that are divisible by 3.

for i in range(1, 51):
    if i % 3 == 0:
        print(i)



# 15. Factorial

# Calculate the factorial of 5.

number = 5
factorial = 1

for i in range(1, number +1):
    factorial *= i

print(factorial)    


# 16. while loop

# Print numbers from 1 to 10 using a while loop.

i = 1

while i <= 10:
    print(i)
    i +=1


# 17. Countdown using while

# Print numbers from 10 down to 1.    

i = 10

while i >= 1:
    print(i)
    i -=1


# 18. Keep asking for a password

# Keep asking the user for a password until they enter "python123". 

password = ""

while password != "python123":
    password = input("Enter password:")

print("Correct password")    


# 19. Sum until the user enters 0

# Keep asking the user for numbers and add them together. Stop when they enter 0.

total = 0


while True:
    number = int(input("enter the number:"))

    if number == 0:
        break

    total += number

print("Total:" , total)   



# 20. Guess the number

# Set:

# secret = 7

# Keep asking the user to guess until they get it correct.

secret = 7

while True:
    number = int(input("Guess the number:"))

    if number == secret:
        print("Correct! You guessed it.")
        break
    else:
        print("Try again")  


# 🔴 Level 3 — Intermediate/Advanced (21–30)
# 21. Use break

# Print numbers from 1 to 100, but stop when you reach 50.          

for i in range(1,102):
    if i == 50:
        break
    print(i)


# 22. Use continue

# Print numbers from 1 to 20, but skip even numbers.    
for i in range(1, 20):
    if i % 2 == 0:
        continue
    print(i)


# 23. Find the first number divisible by 7

# Check numbers from 1 to 100 and stop at the first number divisible by 7.

for i in range( 1,101):
    if i % 7 == 0:
        print(i)
        break
   
# 24. Find all numbers divisible by both 3 and 5

# Print numbers from 1 to 100 that are divisible by both 3 and 5.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# 25. Find the largest number

# Ask the user to enter 5 numbers and find the largest.
   


largest = None

for i in range(5):
    number = int(input("Enter a number: "))

    if largest is None or number > largest:
        largest = number

print("Largest:", largest)




# 26. Count positive, negative, and zero

# Ask the user for 10 numbers and count how many are:

# Positive
# Negative
# Zero

Positive = 0
Negative = 0
Zero = 0

for i in range(10):
    number = int(input("Enter the 10 number"))

    if number > 0:
        Positive +=1
    elif number < 0:
        Negative += 1
    else:
        Zero +=  1

print("Positive:", Positive)
print("Negative:", Negative)
print("Zero:", Zero)      




# 27. Prime number checker

# Ask the user for a number and determine whether it is prime.

number = int(input("Enter a number:"))

if number < 2:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break   

    if is_prime:
        print("Prime")
    else:
        print("Not prime")


#     28. Print prime numbers

# Print all prime numbers between 1 and 100.    

for number in range(2, 101):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)



# 29. Number guessing game with limited attempts

# Create a guessing game where:

# Secret number = 25
# User gets 5 attempts
# Tell them "Too high" or "Too low"
# Stop when they guess correctly
# If they use all attempts, say "Game over"       
# 

secret = 25

for attempt in range(5):
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct! You won!")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")
else:
    print("Game over!")



# 🔥 30. Advanced Challenge — Mini ATM

# Create an ATM program.

# The program starts with:

# balance = 10000

# Show this menu repeatedly:

# 1. Check balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

# Rules:

# Check balance → show current balance
# Deposit → add money
# Withdraw → subtract money only if there is enough balance
# Exit → stop the program
# Invalid choice → show "Invalid choice"

balance = 10000

while True:
    print("\n1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print("Withdrawal successful")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")       
           