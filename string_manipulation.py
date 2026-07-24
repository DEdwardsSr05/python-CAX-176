# David Edwards
# 2026-CAX-176
# July 24, 2026
# ALAB 356.2 - Task 1: String Manipulation Challenge


"""
Goal: take a user's sentence and perform 4 separate string operations on it.
Strings in Python are IMMUTABLE - none of these methods change the original
string in place. Each one returns a brand new string, which is why we print
the result of the method call rather than expecting `sentence` itself to change.
"""

# input() always returns a string, so no int()/float() casting needed -
# we're working with text from the start.
sentence = input("Enter a sentence: ")

# --- 1. Uppercase ---
# .upper() returns a new string with every letter capitalized.
# Non-letter characters (spaces, punctuation, numbers) are left alone.
uppercase_version = sentence.upper()
print("Uppercase:", uppercase_version)

# --- 2. Reversed ---
# This uses slice notation: [start:end:step]
# Leaving start and end blank means "the whole string," and step = -1
# means "walk backward one character at a time" - which reverses it.
# (This is the same [::2] / [1::2] slicing you were just asking about,
# just with a negative step instead of a positive one.)
reversed_version = sentence[::-1]
print("Reversed:", reversed_version)

# --- 3. Vowel count ---
# We loop through every character in the sentence (direct iteration,
# same pattern as "for character in the_string" from your notes).
# For each character, we check if its lowercase version is in our
# string of vowels. Using .lower() here means "A" and "a" both count -
# without it, we'd only catch lowercase vowels.
vowels = "aeiou"
vowel_count = 0
for char in sentence:
    if char.lower() in vowels:
        vowel_count += 1  # augmented assignment - same as vowel_count = vowel_count + 1

print("Vowel count:", vowel_count)

# --- 4. Replace spaces with hyphens ---
# .replace(old, new) returns a new string with every occurrence of
# `old` swapped for `new`. It's a straight find-and-replace, no loop needed.
hyphenated_version = sentence.replace(" ", "-")
print("Hyphenated:", hyphenated_version)
