# David Edwards
# 2026-CAX-176
# July 21, 2026
# ALAB 353.3
# bubble_sort_demo.py
# Implements bubble sort: repeatedly compares adjacent pairs and swaps them if out of order.
# After each full pass, the largest unsorted element "bubbles up" to its correct position.

numbers = [64, 25, 12, 22, 11]
print("Starting list:", numbers)

n = len(numbers)

# Outer loop: controls how many passes we make through the list.
# Each pass guarantees one more element is in its final sorted position,
# so we can shrink the range we check each time (n - i - 1).
for i in range(n):
    swapped = False  # tracks if any swap happened this pass — if not, list is already sorted

    # Inner loop: compares each adjacent pair up to the unsorted portion
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap using Python's tuple-unpacking trick — no temp variable needed
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True

    print(f"After pass {i + 1}: {numbers}")

    # If no swaps happened, the list is fully sorted early — no need to keep looping
    if not swapped:
        break

print("Final sorted list:", numbers)