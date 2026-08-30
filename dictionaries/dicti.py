"""
PYTHON DICTIONARY PRACTICE - 20 QUESTIONS (Beginner to Advanced)
Each question has a solution right below it. Run this file directly in VS Code.
"""

# ============================================================
# BEGINNER LEVEL (Q1 - Q7)
# ============================================================

# Q1. Create a dictionary with keys 'name', 'age', 'city' and print it.
person = {"name": "Roy", "age": 22, "city": "Kathmandu"}
print("Q1:", person)


# Q2. Access the value of key 'name' from the dictionary above.
print("Q2:", person["name"])


# Q3. Add a new key 'country' with value 'Nepal' to the dictionary.
person["country"] = "Nepal"
print("Q3:", person)


# Q4. Update the value of 'age' to 23.
person["age"] = 23
print("Q4:", person)


# Q5. Remove the key 'city' from the dictionary.
person.pop("city")
print("Q5:", person)


# Q6. Check if the key 'name' exists in the dictionary.
print("Q6:", "name" in person)


# Q7. Loop through the dictionary and print all key-value pairs.
print("Q7:")
for key, value in person.items():
    print(f"   {key}: {value}")


# ============================================================
# INTERMEDIATE LEVEL (Q8 - Q14)
# ============================================================

# Q8. Given a list of words, count the frequency of each word using a dictionary.
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}
for w in words:
    word_count[w] = word_count.get(w, 0) + 1
print("Q8:", word_count)


# Q9. Merge two dictionaries into one.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}
print("Q9:", merged)


# Q10. Find the key with the maximum value in a dictionary.
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
top_scorer = max(scores, key=scores.get)
print("Q10:", top_scorer, "->", scores[top_scorer])


# Q11. Swap keys and values in a dictionary.
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print("Q11:", swapped)


# Q12. Sort a dictionary by its values (ascending).
unsorted_dict = {"banana": 3, "apple": 1, "cherry": 2}
sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))
print("Q12:", sorted_dict)


# Q13. Create a dictionary from two separate lists (keys and values).
keys = ["id", "name", "role"]
values = [101, "Roy", "Developer"]
combined = dict(zip(keys, values))
print("Q13:", combined)


# Q14. Filter a dictionary to keep only items where value > 2.
data = {"a": 1, "b": 5, "c": 3, "d": 2}
filtered = {k: v for k, v in data.items() if v > 2}
print("Q14:", filtered)


# ============================================================
# ADVANCED LEVEL (Q15 - Q20)
# ============================================================

# Q15. Given a nested dictionary, access a deeply nested value safely.
nested = {
    "user": {
        "profile": {
            "name": "Roy",
            "email": "roy@example.com"
        }
    }
}
email = nested.get("user", {}).get("profile", {}).get("email", "Not Found")
print("Q15:", email)


# Q16. Group a list of dictionaries by a common key (e.g., group students by grade).
students = [
    {"name": "Roy", "grade": "A"},
    {"name": "Sam", "grade": "B"},
    {"name": "Kim", "grade": "A"},
    {"name": "Lee", "grade": "B"},
]
grouped = {}
for student in students:
    grade = student["grade"]
    grouped.setdefault(grade, []).append(student["name"])
print("Q16:", grouped)


# Q17. Find common keys between two dictionaries.
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}
common_keys = d1.keys() & d2.keys()
print("Q17:", common_keys)


# Q18. Flatten a nested dictionary into a single-level dictionary
#      (e.g., {'a': {'b': 1}} -> {'a.b': 1})
def flatten_dict(d, parent_key="", sep="."):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

nested_data = {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
print("Q18:", flatten_dict(nested_data))


# Q19. Count frequency of characters in a string using a dictionary, ignoring spaces.
text = "hello world"
char_freq = {}
for ch in text:
    if ch != " ":
        char_freq[ch] = char_freq.get(ch, 0) + 1
print("Q19:", char_freq)


# Q20. Implement a simple LRU-style cache using a dictionary
#      (removes the oldest item when capacity is exceeded).
class SimpleLRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []  # tracks insertion order

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.order.pop(0)
            del self.cache[oldest]
        self.cache[key] = value
        self.order.append(key)

    def get(self, key):
        return self.cache.get(key, "Not Found")

    def __repr__(self):
        return str(self.cache)


lru = SimpleLRUCache(capacity=3)
lru.put("a", 1)
lru.put("b", 2)
lru.put("c", 3)
lru.put("d", 4)  # this should evict 'a' since capacity is 3
print("Q20:", lru)