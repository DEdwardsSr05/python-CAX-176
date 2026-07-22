# David Edwards
# 2026-CAX-176
# July 21, 2026
# ALAB 353.3
# list_operations.py
# Demonstrates common list operations: sorting (both ways), appending, removing, reversing

numbers = [42, 17, 8, 99, 23]
print("Original list:", numbers)

# sorted() returns a NEW sorted list — the original list is untouched
sorted_copy = sorted(numbers)
print("Sorted list (using sorted(), original untouched):", sorted_copy)
print("Original list still unchanged:", numbers)

# .sort() sorts the list IN PLACE — no new list, modifies 'numbers' directly, returns None
numbers.sort()
print("Sorted list (using .sort(), in place):", numbers)

# .append() adds a single item to the end of the list
numbers.append(100)
print("List after appending 100:", numbers)

# .remove(value) deletes the first matching value it finds (not by index)
numbers.remove(8)
print("List after removing the value 8:", numbers)

# .reverse() flips the list order in place
numbers.reverse()
print("List after reversing:", numbers)