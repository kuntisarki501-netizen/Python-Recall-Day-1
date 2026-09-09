
# BEGINNER
# 1. Create a string
# Create a variable called name and store your name in it.
# Print the name.


# Solution:
name = "Ram"

print(name)


# 2. Find the length
# Find the number of characters in:
#
# text = "Python"
#
# Use len().


# Solution:
text = "Python"

print(len(text))


# 3. Access the first character
# Print the first character of:
#
# word = "Python"


# Solution:
word = "Python"

print(word[0])


# 4. Access the last character
# Print the last character using negative indexing.


# Solution:
word = "Python"

print(word[-1])


# 5. String slicing
# Print "Pyt" from:
#
# word = "Python"


# Solution:
word = "Python"

print(word[0:3])


# 6. Convert to uppercase
# Convert:
#
# text = "hello world"
#
# to uppercase.


# Solution:
text = "hello world"

print(text.upper())


# 7. Convert to lowercase
# Convert:
#
# text = "PYTHON PROGRAMMING"
#
# to lowercase.


# Solution:
text = "PYTHON PROGRAMMING"

print(text.lower())



# 8. Remove spaces
# Remove spaces from the beginning and end of:
#
# text = "   Python   "
#
# Use strip().


# Solution:
text = "   Python   "

print(text.strip())

#  INTERMEDIATE


# 9. Replace text
# Replace "Java" with "Python":
#
# text = "I am learning Java"


# Solution:
text = "I am learning Java"

new_text = text.replace("Java", "Python")

print(new_text)


# 10. Count a character
# Count how many times "a" appears:
#
# text = "banana"


# Solution:
text = "banana"

print(text.count("a"))


# 11. Find a word
# Find the position of "Python":
#
# text = "I am learning Python"


# Solution:
text = "I am learning Python"

print(text.find("Python"))



# 12. Check if a word exists
# Check whether "Python" exists in:
#
# text = "I am learning Python"


# Solution:
text = "I am learning Python"

if "Python" in text:
    print("Python exists")
else:
    print("Python does not exist")



# 13. Split a sentence
# Convert:
#
# text = "Python is easy to learn"
#
# into a list of words using split().


# Solution:
text = "Python is easy to learn"

words = text.split()

print(words)



# 14. Join a list
# Given:
#
# words = ["Python", "is", "fun"]
#
# Join them into:
#
# "Python is fun"


# Solution:
words = ["Python", "is", "fun"]

sentence = " ".join(words)

print(sentence)


# 15. Count vowels
# Count the number of vowels in:
#
# text = "Python programming"
#
# Vowels are:
# a, e, i, o, u


# Solution:
text = "Python programming"

count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print("Vowels:", count)


# ADVANCED


# 16. Reverse a string
# Reverse:
#
# text = "Python"
#
# without using reversed().


# Solution:
text = "Python"

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)


# 17. Check palindrome
# Create a program that checks whether a word
# is a palindrome.
#
# Example:
# madam -> Palindrome
# python -> Not palindrome


# Solution:
word = input("Enter a word: ")

reversed_word = word[::-1]

if word == reversed_word:
    print("Palindrome")
else:
    print("Not palindrome")



# 18. Count words in a sentence
# Ask the user to enter a sentence.
# Count how many words are in the sentence.


# Solution:
sentence = input("Enter a sentence: ")

words = sentence.split()

print("Number of words:", len(words))



# 19. Character frequency
# Ask the user to enter a word.
# Count how many times each character appears.
#
# Example:
#
# Input:
# banana
#
# Output:
# b = 1
# a = 3
# n = 2
#
# Use a dictionary.


# Solution:
word = input("Enter a word: ")

frequency = {}

for char in word:

    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char, count in frequency.items():
    print(char, "=", count)

# 20. ADVANCED CHALLENGE
#
# Create a username/password checker.
#
# Ask the user for a username and password.
#
# Rules:
#
# 1. Username must contain at least 5 characters.
# 2. Password must contain at least 8 characters.
# 3. Password must contain at least one number.
# 4. Password must contain at least one uppercase letter.
#
# Print whether the password is valid or invalid.


# Solution:
username = input("Enter username: ")
password = input("Enter password: ")

username_valid = len(username) >= 5
password_length = len(password) >= 8
has_number = False
has_uppercase = False

for char in password:

    if char.isdigit():
        has_number = True

    if char.isupper():
        has_uppercase = True


if username_valid and password_length and has_number and has_uppercase:
    print("Username and password are valid")
else:
    print("Invalid username or password")