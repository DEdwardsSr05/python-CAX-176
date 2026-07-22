# David Edwards
# 2026-CAX-176
# July 21, 2026
# ALAB 353.4
# tuples_dicts.py
# Demonstrates tuple immutability and dictionary key-value operations

# --- TUPLES ---
months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

print("First month:", months[0])
print("Last month:", months[-1])   # -1 always refers to the last item, regardless of length

# Tuples are immutable — trying to change an element raises a TypeError.
# We catch it here to prove/demonstrate that behavior instead of crashing.
try:
    months[0] = "NewMonth"
except TypeError as e:
    print(f"Tuples are immutable, error: {e}")

# --- DICTIONARIES ---
students = {
    "Alice": 90,
    "Bob": 78,
    "Carlos": 85
}

# Adding a new key-value pair — dictionaries grow dynamically, no fixed size like tuples
students["Diana"] = 92
print("\nAfter adding Diana:", students)

# Updating an existing value — just reassign to the same key
students["Bob"] = 82
print("After updating Bob's grade:", students)

# Looping over a dictionary with .items() gives you both key and value at once
print("\nAll students and grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")