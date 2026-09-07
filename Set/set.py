


#  BEGINNER


# 1. Create a set
# Create a set containing:
# apple, banana, mango
#
# Print the set.


# Solution:
fruits = {"apple", "banana", "mango"}

print(fruits)



# 2. Create a set with duplicate values
# Create:
#
# numbers = {1, 2, 2, 3, 3, 4, 4}
#
# Print the set.
#
# What do you notice?


# Solution:
numbers = {1, 2, 2, 3, 3, 4, 4}

print(numbers)



# 3. Check the type
# Print the type of:
#
# numbers = {1, 2, 3}


# Solution:
numbers = {1, 2, 3}

print(type(numbers))



# 4. Find the length
# Find the number of items in:
#
# fruits = {"apple", "banana", "mango", "orange"}


# Solution:
fruits = {"apple", "banana", "mango", "orange"}

print(len(fruits))



# 5. Check if an item exists
# Check whether "banana" exists in:
#
# fruits = {"apple", "banana", "mango"}


# Solution:
fruits = {"apple", "banana", "mango"}

if "banana" in fruits:
    print("Banana exists")
else:
    print("Banana does not exist")



# 6. Add an item
# Add "orange" to:
#
# fruits = {"apple", "banana", "mango"}


# Solution:
fruits = {"apple", "banana", "mango"}

fruits.add("orange")

print(fruits)



# 7. Remove an item
# Remove "banana" from:
#
# fruits = {"apple", "banana", "mango"}


# Solution:
fruits = {"apple", "banana", "mango"}

fruits.remove("banana")

print(fruits)


# 8. Loop through a set
# Print every item:
#
# fruits = {"apple", "banana", "mango"}


# Solution:
fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)



#  INTERMEDIATE


# 9. Remove duplicates from a list
# Given:
#
# numbers = [1, 2, 2, 3, 4, 4, 5, 5]
#
# Convert the list into a set to remove duplicates.


# Solution:
numbers = [1, 2, 2, 3, 4, 4, 5, 5]

unique_numbers = set(numbers)

print(unique_numbers)



# 10. Set union
# Given:
#
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
#
# Find all values from both sets.


# Solution:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.union(set2)

print(result)


# 11. Set intersection
# Given:
#
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
#
# Find the values that exist in BOTH sets.


# Solution:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.intersection(set2)

print(result)



# 12. Set difference
# Given:
#
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
#
# Find the values that are in set1
# but NOT in set2.


# Solution:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.difference(set2)

print(result)



# 13. Symmetric difference
# Given:
#
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
#
# Find values that exist in only one of the sets.


# Solution:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)

print(result)



# 14. Update a set
# Add all values from set2 into set1.
#
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}


# Solution:
set1 = {1, 2, 3}
set2 = {4, 5, 6}

set1.update(set2)

print(set1)



# 15. Find common students
# Given:
#
# python_students = {"Ram", "Sita", "Hari", "John"}
# java_students = {"Hari", "John", "Gita", "Sam"}
#
# Find students who study BOTH Python and Java.


# Solution:
python_students = {"Ram", "Sita", "Hari", "John"}
java_students = {"Hari", "John", "Gita", "Sam"}

common = python_students.intersection(java_students)

print(common)



# ADVANCED


# 16. Find students who only study Python
# Using the same sets:
#
# python_students = {"Ram", "Sita", "Hari", "John"}
# java_students = {"Hari", "John", "Gita", "Sam"}
#
# Find students who study Python
# but NOT Java.


# Solution:
python_students = {"Ram", "Sita", "Hari", "John"}
java_students = {"Hari", "John", "Gita", "Sam"}

only_python = python_students.difference(java_students)

print(only_python)


# 17. Find students who study only one language
# Find students who study Python OR Java,
# but NOT both.


# Solution:
python_students = {"Ram", "Sita", "Hari", "John"}
java_students = {"Hari", "John", "Gita", "Sam"}

only_one = python_students.symmetric_difference(java_students)

print(only_one)



# 18. Remove duplicates from user input
# Ask the user to enter 5 numbers.
#
# Store them in a list.
# Convert the list to a set.
# Print the unique numbers.


# Solution:
numbers = []

for i in range(5):
    number = int(input("Enter number: "))
    numbers.append(number)

unique_numbers = set(numbers)

print("Unique numbers:", unique_numbers)



# 19. Check subset
# Given:
#
# A = {1, 2}
# B = {1, 2, 3, 4, 5}
#
# Check whether A is a subset of B.


# Solution:
A = {1, 2}
B = {1, 2, 3, 4, 5}

if A.issubset(B):
    print("A is a subset of B")
else:
    print("A is not a subset of B")



# 20. ADVANCED CHALLENGE
#
# Create a program that compares two lists of students.
#
# list1 = ["Ram", "Sita", "Hari", "John", "Gita"]
# list2 = ["Hari", "John", "Sam", "Gita", "David"]
#
# Find:
#
# 1. Students in both lists
# 2. Students only in list1
# 3. Students only in list2
# 4. All unique students
#
# Use SETS to solve the problem.


# Solution:
list1 = ["Ram", "Sita", "Hari", "John", "Gita"]
list2 = ["Hari", "John", "Sam", "Gita", "David"]

students1 = set(list1)
students2 = set(list2)

both = students1.intersection(students2)

only_list1 = students1.difference(students2)

only_list2 = students2.difference(students1)

all_students = students1.union(students2)

print("Students in both:", both)
print("Only in list 1:", only_list1)
print("Only in list 2:", only_list2)
print("All students:", all_students)