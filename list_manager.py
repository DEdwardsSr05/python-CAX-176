# David Edwards
# 2026-CAX-176
# July 24, 2026
# ALAB 356.2 - Task 2: List Management with Error Handling


"""
Goal: a menu-driven program that lets the user add, remove, and view
integers in a list, with try/except protecting against bad input.

Two distinct failure modes to catch here:
1. ValueError - user types something that isn't a number when we
   try to int() it (e.g. typing "banana" instead of "5").
2. IndexError - user asks to remove a valid INTEGER index, but one
   that doesn't actually exist in the list (e.g. list has 3 items,
   user asks to remove index 10).
These are different exceptions because they happen at different points:
ValueError happens at int() conversion time; IndexError happens later,
when .pop() actually tries to reach into the list.
"""

numbers = []  # our list of integers - starts empty, single source of truth

menu_text = """
List Manager Menu:
a. Add a number
b. Remove a number
c. Display the list
d. Quit
"""

while True:
    print(menu_text)
    choice = input("Enter your choice (a/b/c/d): ").strip().lower()

    if choice == "a":
        # --- Add a number ---
        raw_input_value = input("Enter an integer to add: ").strip()
        try:
            # int() is where a non-numeric entry blows up with ValueError.
            number = int(raw_input_value)
            numbers.append(number)
            print(f"{number} added. List is now: {numbers}")
        except ValueError:
            # Catches things like "banana" or "5.5" (int() can't parse a decimal).
            print(f"'{raw_input_value}' is not a valid integer. Nothing added.")

    elif choice == "b":
        # --- Remove a number by index ---
        raw_index = input("Enter the index to remove: ").strip()
        try:
            index = int(raw_index)  # can also raise ValueError here
            removed_value = numbers.pop(index)  # can raise IndexError here
            print(f"Removed {removed_value} from index {index}. List is now: {numbers}")
        except ValueError:
            print(f"'{raw_index}' is not a valid integer index.")
        except IndexError:
            # This fires if the index IS a valid integer, but out of range
            # for the current list (e.g. list has 3 items, index 10 given).
            print(f"Index {raw_index} is out of range. List is now: {numbers}")

    elif choice == "c":
        # --- Display the list ---
        if not numbers:  # empty list is "falsy"
            print("The list is currently empty.")
        else:
            print("Current list:", numbers)

    elif choice == "d":
        print("Goodbye!")
        break  # exits the while True loop

    else:
        # Catches any menu input that isn't a/b/c/d
        print("Invalid choice. Please enter a, b, c, or d.")
