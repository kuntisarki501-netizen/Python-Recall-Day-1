# Level 1: Absolute Basics
# Q1. Creaates a variables called city and store thye value "KTM" in it. then print it.
# Sloution

city = "KTM"
print(city)


# Q2. Create two variables a and b with value 10 and 20. Print their sum.
# Solution

a = 10
b = 20
print(a + b)

# Q3. Store your name in a variables, then print a messages like: "My name is <nmae>".
# Solution

name = "Kunti"
print("My name is " + name)

# Q4 Store your marks in three variables and calculate the total.
english = 75
nepali = 60
science = 80

total = english + nepali + science
print(total)


# Level 2:Understanding Variable Types
#Q5. Swap the value of two variables x=5 and y=10. wihout using a third variable
x= 5
y= 10 
x, y =y, x
print(x, y)


#Q6. Create variables of diffrent data types: an integer, a float, a string and a boolean. print each one along with its types using types().
#Solution
class_name = 10
precentage = 99.98
name = "kunti"
is_student = True

print(class_name, type(class_name))
print(precentage, type(precentage))
print(name, type(name))
print(is_student, type(is_student))

#Q7. A variable temp = "25" holds a temperature as a string. Convert it to an integer and add 5 to it.
temp = "25"
temp = int(temp) + 5
print(temp)

#Q8  Cteate a variables and increase its value by 10
num = 50
num +=10
print(num)


# Level 3: Variable Operations

#Q.9 Without running the code, predict the output. Then verify:
a = 5
b = a
a = a + 10
print(a,b)

#Q10. Create two variables and perform: addition, subtraction, multiplication, division

a = 10
b =  20

print(a+b)
print(a-b)
print(a*b)
print(a/b)


#Q12. Find the remainder of two numbers.

a = 17
b = 5
remainder = a % b
print(remainder)

# Q13 Find the square of a number using a variable.

num = 8
square = num ** 2
print(square)


#Q14 Calculate the average of three numbers.

a = 70
b = 80
c = 90

average = (a + b + c) / 3

print(average)

# Level 4: Taking Input into Variables
#Q14. Ask the user for their name and store it in a variable.

name = input("Enter your name:")
print(name)

#Q15. Ask the user for their age and print it.

age = int(input("Enter your age:"))
print(age)

#Q16. Ask for two numbers and calculate their sum.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

total = num1 + num2

print(total)


#Q17 Ask for the user's name, age, and city and display them.

name = input ("Enter your name:")
age = int (input("enter your age:"))
city = input ("Enter your city:")


print("Name:", name)
print("Age:", age)
print("City:", city)

#Level 5: Variable Reassignment

#Q18. Create balance = 1000. Add 500 to it.

balance = 1000
balance += 500

print(balance)

#Q19. Create score = 100. Subtract 25.

score = 100
score -= 25

print(score)

#Q20. Create price = 100. Increase the price by 10%.

price = 100
price = price + (price * 10 / 100)
print(price)

# Level 6: Variable Naming
#Q21. Which variable names are valid?
#NOTE:

# name
# student_name
# student1
# 1student
# student-name
# _age
# class


# Valid:

# name
# student_name
# student1
# _age

# Level 8: Strings and Variables
# Q22. Store first name and last name in separate variables and combine them.

first_name = "kunti"
last_name = "Sarki"

full_name = first_name + " " + last_name
print(full_name)

# Q23. Create a variable containing your age and print:

age = 21

print(f"I am {age} years old")

#Q28. Store price and quantity in variables and calculate total price.
price = 100
quantity = 5

total = price * quantity

print(total)

# Level 9: Real Problems
#Q29.
# Take:

# student name
# English marks
# Math marks
# Science marks

# Calculate:

# total
# average

# Solution:

student_name = input("enter your name:")
English_marks = int(input ("enter your english mark:"))
Math_marks = int(input ("enter your math mark:"))
Science_marks = int(input ("enter your science mark:"))

total = English_marks + Math_marks + Science_marks
average = total/3

print(total)
print(average)
print("student:",student_name)
print("Mark_eng:",English_marks)
print("Mark_math:",Math_marks)
print("Mark+sci:",Science_marks)


#Q30.
# A product costs 500 and the customer buys 3.

# Calculate the total bill.

price = 500
quantity = 3
total = price * quantity
print("Total bill:", total)

#Q31. Temperature Conversion

# Store Celsius in a variable and convert it to Fahrenheit.

celsius = 30
fahrenheit = (30 *9/5) + 32
print("Fahrenheit:", fahrenheit)


#Q32. Calculate Simple Interest

Principal = 10000
rate = 5
time = 2

SI = (10000 *5*2)
print("Simple Interest:", SI )


#Level 10: Advanced Practice

# Q33. Create a banking system using variables.

# balance = 5000

# Deposit 2000, then withdraw 1500.

balance = 5000
balance +=2000
balance -=1500

print("Final Balance:", balance)


# Q34. Create a salary calculator.
Basic_salary = 30000
Bonus = 5000
Tax = 3000

total_Salary = Basic_salary + Bonus + Tax
print("Total Salary:", total_Salary)

# Q35. Create a BMI calculator.

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print("BMI:", bmi)


# Level 12: Challenge Questions

# Q36. Employee Information

# Create variables for:

# name
# age
# department
# salary
# experience

# Print all information in a clean format.

name = "kunti"
age = 24
department = "Data Science"
salary = 10000
experience = 3

print("Employee Information")
print("Name:", name)
print("Age:", age)
print("Department:", department)
print("Salary:", salary)
print("Experience:", experience, "year")


# Q42. Digital Wallet

# Start with:

wallet = 5000
wallet +=2000
wallet -=1500
wallet +=1000
wallet -=500

print("Final_wallet:", wallet)