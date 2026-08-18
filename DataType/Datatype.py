# Datatype
#LEVEL 1: Basic Practice

# Q1. Identify the data type

x = 25
print(type(x))


name = "Python"
print(type(name))

# Q2.

# Create variables for:

# your name
# your age
# your height
# whether you are a student

# Print their data types.

name = "Kunti"
age = 22
height = 5.8
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# LEVEL 2: Strings and Numbers

# Q3. What will this produce?
x = 10
y = 5

print(x + y)


x = 10
y = 2.5

print(x + y)


x = "10"
y = "20"

print(x + y)


# Q4. Convert this string into an integer:

age = "22"
age = int(age)

print(age)
print(type(age))


price = "99.50"
price = float(price)
print(price)
print(type(price))


# LEVEL 3: Type Conversion

# Python provides functions for converting data types.

# int()
# float()
# str()
# bool()
# list()
# tuple()
# set()

x = "10"
y = 5

print(int(x) + y)



x = 10
y = "5"

print(x +int(y))

age = 22
age = "22"
print(age)
print(type(age))


# LEVEL 4: List, Tuple, Set

# Q15. Identify the types

a = [1, 2, 3]
b = (1, 2, 3)
c = {1, 2, 3}

print(type(a))
print(type(b))
print(type(c))


# Q16.  Create a list containing: [LIST]

# Python
# SQL
# Power BI
# Excel

skill = ["Python", "SQL", "Power" ,"BI", "Excel"]
print(skill)


skills = ["Python", "SQL", "Power" ,"BI", "Excel"]
skills.append("Tableau")
skills.remove("SQL")
print(skills)

skill = ["Python", "SQL", "Power" ,"BI", "Excel"]
skill[2]= "CSS"
print(skill)

#[SET]

number = {1,2,3,4,1,2}
print(number)

number.add(4)
number.remove(1)
print(number)


#[TUPLES]
# Q19.

# Why does this fail?

# languages = ("Python", "SQL", "PHP")


# languages[0] = "Java"
# Solution

# Because a tuple is immutable.

# You cannot modify an existing tuple element.

# (No — you cannot add or remove items from a tuple directly. Tuples are immutable, meaning once created, their contents cannot be changed in any way (no adding, removing, or modifying items).)


# LEVEL 5: Dictionary

# Dictionary in Python

# A dictionary is a collection that stores data as key-value pairs, instead of just single items like lists/tuples/sets. Think of it like a real dictionary — you look up a word (key) to get its meaning (value).

# Mutable (can add, remove, change items)
# Keys must be unique (no duplicate keys — but values can repeat)
# Keys must be immutable (strings, numbers, tuples — not lists)
# Written with curly brackets {}, but with key: value pairs

student = {"name":"kunti", "age": 23, "city": "KTM"}
print(student)

# Q21. Print only the student's name.
 
student = {"name":"kunti", "age": 23, "city": "KTM"}
print(student["name"])


# Q22. Change the age to 23.
student = {"name":"kunti", "age": 23, "city": "KTM"}

student["age"] =25
print(student)

# Q23. Add a new key:

student = {"name":"kunti", "age": 23, "city": "KTM"}
student["course"]= "Data Science"
print(student)


# LEVEL 6: Mixed Data Types

# Q24. What are the data types?

name = "Alex"
age = 25
height = 5.9
skills = ["Python", "SQL"]
address = ("Kathmandu", "Nepal")
is_working = False

print(type(name))
print(type(age))
print(type(height))
print(type(address))
print(type(is_working))



# Q25.

# Create one variable containing:

# name = "Alex"
# age = 25
# marks = 87.5
# passed = True

# using a list.

student = ["Alex", 25, 87.5, True]

print(student)


# LEVEL 7: Understanding type() and isinstance()

# Q26. What is the difference?
x= 10
type(x)

isinstance(x, int)

# (I) Type()
X = 10
print(type(x))
print(type(x) == int)


name = "Ali"
print(type(name))


# (II) isinstance()

# Checks if an object is an instance of a type (or class) — returns True/False. 
# It's the preferred way to check types in real code.

x = 10
print(isinstance(x, int))         
print(isinstance(x, str))    


# Rule of thumb: Use isinstance() in almost all real-world code — it's safer and handles inheritance correctly. 
# Use type() only when you specifically need the exact class, not a subclass.


# Q27. Write a program that checks whether age is an integer.


age = 23
print(isinstance(age, int))   # this code show true

age = 23
print(isinstance(age, str))   # this shoe false



# LEVEL 8: Tricky Questions

# Q28. What is the type of:

x = 10/2
print(type(x))


y = 20 // 5
print(type(x))



# LEVEL 9: Advanced Data Type Practice

# Q32. What is the final value?

# x = "10"
# x = int(x)
# x = x + 5
# x = str(x)

# print(x)
# print(type(x))

x = "10"
x = int(x)
x = x + 5
x = str(x)

print(x)
print(type(x))


# Q33. What happens?

data = [1, 2, 2, 3, 3, 4]

unique_data = set(data)  # remove the duplicate from the ,list

print(unique_data)



# Q34. Convert this list into a tuple:

num = [10, 20, 30]
num = tuple(num)
print(num)
print(type(num))


# Q35. Convert this tuple into a list:
number= (1, 2, 3, 4)
number = list(number)
print(number)
print(type(number))


# LEVEL 10: Challenge Questions

# Try these without looking at the solutions first.

# Create variables for:

# name
# age
# department
# salary
# experience

# Print each value and its data type.

name = "kunti"
age = 24
department = "BCS"
salary = 20000
experience = 3

print(name, type(name))
print(age, type(age))
print(department, type(department))
print(salary, type(salary))
print(experience, type(experience))


# Q37. Type Conversion Challenge

# age = "22"
# salary = "45000.50"
# experience = "2"

age = int(age)
salary = float(salary)
experience = int(experience)

print(age)
print(salary)
print(experience)



# Q38. Student Data

# Create a dictionary:

# name
# age
# marks
# passed
# subjects

# where subjects is a list.

student = {
"name" : "Kunti",
"age" : 25,
"marks" : 90.5 ,
"subjects": ["Python", "SQL", "Data Science"]
}

print(student)


# Q40. Final Challenge

# What will this print?

x = "100"
y = 50
z = 2.5

x = int(x)
result = x + y + z

print(result)
print(type(result))