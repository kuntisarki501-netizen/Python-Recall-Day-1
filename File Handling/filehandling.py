


#  BEGINNER


# 1. Create and write to a file
# Create a file called "hello.txt"
# and write "Hello Python!" into it.
#
# Use write mode "w".


# Solution:
file = open("hello.txt", "w")

file.write("Hello Python!")

file.close()



# 2. Read a file
# Read the contents of "hello.txt"
# and print them.


# Solution:
file = open("hello.txt", "r")

content = file.read()

print(content)

file.close()



# 3. Write multiple lines
# Create a file called "students.txt"
# and write three student names:
#
# Ram
# Sita
# Hari


# Solution:
file = open("students.txt", "w")

file.write("Ram\n")
file.write("Sita\n")
file.write("Hari\n")

file.close()


# 4. Read the entire file
# Read and print everything from:
#
# students.txt


# Solution:
file = open("students.txt", "r")

content = file.read()

print(content)

file.close()



# 5. Read one line
# Read only the first line from:
#
# students.txt


# Solution:
file = open("students.txt", "r")

line = file.readline()

print(line)

file.close()



# 6. Read all lines
# Read all lines from students.txt
# and store them in a list.


# Solution:
file = open("students.txt", "r")

lines = file.readlines()

print(lines)

file.close()



# 7. Append to a file
# Add "Gita" to the end of students.txt
# without deleting the existing students.


# Solution:
file = open("students.txt", "a")

file.write("Gita\n")

file.close()



# 8. Check file contents
# Open students.txt and print each student
# on a separate line using a loop.


# Solution:
file = open("students.txt", "r")

for line in file:
    print(line.strip())

file.close()



# 🟡 INTERMEDIATE


# 9. Use "with open"
# Rewrite question 2 using:
#
# with open(...)
#
# so you don't need to manually call close().


# Solution:
with open("hello.txt", "r") as file:
    content = file.read()

print(content)


# 10. Count lines
# Count how many lines are inside:
#
# students.txt


# Solution:
with open("students.txt", "r") as file:
    lines = file.readlines()

print("Number of lines:", len(lines))



# 11. Count words
# Create a file called "sentence.txt"
# containing:
#
# Python is easy to learn
#
# Read the file and count the number of words.


# Solution:
with open("sentence.txt", "w") as file:
    file.write("Python is easy to learn")


with open("sentence.txt", "r") as file:
    text = file.read()

words = text.split()

print("Number of words:", len(words))



# 12. Count characters
# Read sentence.txt and count the number
# of characters in the file.


# Solution:
with open("sentence.txt", "r") as file:
    text = file.read()

print("Characters:", len(text))


# 13. Search for a word
# Ask the user for a word.
# Check whether that word exists in sentence.txt.


# Solution:
search_word = input("Enter word to search: ")

with open("sentence.txt", "r") as file:
    text = file.read()

if search_word in text:
    print("Word found")
else:
    print("Word not found")



# 14. Copy a file
# Read everything from:
#
# hello.txt
#
# and write it into:
#
# copy.txt


# Solution:
with open("hello.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as destination:
    destination.write(content)

print("File copied successfully")



# ADVANCED


# 15. Store numbers in a file
# Create numbers.txt containing:
#
# 10
# 20
# 30
# 40
# 50
#
# Read the numbers from the file
# and calculate their total.


# Solution:
with open("numbers.txt", "w") as file:
    file.write("10\n")
    file.write("20\n")
    file.write("30\n")
    file.write("40\n")
    file.write("50\n")


total = 0

with open("numbers.txt", "r") as file:

    for line in file:
        number = int(line.strip())
        total += number

print("Total:", total)


# 16. Find the largest number from a file
# Read numbers.txt and find the largest number.
#
# Do NOT use max().


# Solution:
largest = None

with open("numbers.txt", "r") as file:

    for line in file:
        number = int(line.strip())

        if largest is None or number > largest:
            largest = number

print("Largest:", largest)



# 17. Save user information
# Ask the user for:
#
# Name
# Age
# Country
#
# Save the information into user.txt.


# Solution:
name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")

with open("user.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Country: " + country + "\n")

print("Information saved!")



# 18. Simple login system
#
# Create a file called users.txt.
#
# Store:
#
# ram,password123
# sita,hello456
#
# Ask the user for a username and password.
#
# Check the file and determine whether
# the login information is correct.


# Solution:
with open("users.txt", "w") as file:
    file.write("ram,password123\n")
    file.write("sita,hello456\n")


username = input("Username: ")
password = input("Password: ")

login_success = False

with open("users.txt", "r") as file:

    for line in file:

        line = line.strip()

        stored_username, stored_password = line.split(",")

        if username == stored_username and password == stored_password:
            login_success = True
            break


if login_success:
    print("Login successful")
else:
    print("Invalid username or password")


# 19. Student marks file
#
# Create marks.txt:
#
# Ram,80
# Sita,95
# Hari,70
# Gita,85
#
# Read the file and:
#
# 1. Print every student
# 2. Find the highest mark
# 3. Find the average mark


# Solution:
with open("marks.txt", "w") as file:
    file.write("Ram,80\n")
    file.write("Sita,95\n")
    file.write("Hari,70\n")
    file.write("Gita,85\n")


students = []

with open("marks.txt", "r") as file:

    for line in file:

        line = line.strip()

        name, mark = line.split(",")

        mark = int(mark)

        students.append((name, mark))


total = 0
highest = students[0]

print("Students:")

for name, mark in students:

    print(name, "-", mark)

    total += mark

    if mark > highest[1]:
        highest = (name, mark)


average = total / len(students)

print()
print("Highest:", highest)
print("Average:", average)



# 20. ADVANCED MINI PROJECT
#
# Create a simple Notes App.
#
# The program should have:
#
# 1. Add note
# 2. View notes
# 3. Search note
# 4. Exit
#
# Notes should be saved inside:
#
# notes.txt
#
# The notes must still exist after
# the program is closed.


# Solution:
while True:

    print("\n===== NOTES APP =====")
    print("1. Add note")
    print("2. View notes")
    print("3. Search note")
    print("4. Exit")

    choice = input("Choose: ")


    # Add note
    if choice == "1":

        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note saved!")


    # View notes
    elif choice == "2":

        try:

            with open("notes.txt", "r") as file:

                notes = file.readlines()

                if len(notes) == 0:
                    print("No notes found.")

                else:

                    print("\nYour Notes:")

                    for i, note in enumerate(notes, start=1):
                        print(i, "-", note.strip())

        except FileNotFoundError:

            print("No notes found.")


    # Search note
    elif choice == "3":

        search = input("Enter word to search: ")

        try:

            with open("notes.txt", "r") as file:

                found = False

                for note in file:

                    if search.lower() in note.lower():

                        print("Found:", note.strip())

                        found = True

                if not found:
                    print("No matching note found.")

        except FileNotFoundError:

            print("No notes found.")


    # Exit
    elif choice == "4":

        print("Goodbye!")

        break


    else:

        print("Invalid choice")