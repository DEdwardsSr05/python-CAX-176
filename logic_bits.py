# David Edwards
# 2026-CAX-176
# July 21, 2026
# ALAB 353.3
# logic_bits.py
# Bonus: demonstrates logical operators (and, or, not) and bitwise operators (&, |, ^, ~, <<, >>)

# --- LOGICAL OPERATORS ---
a = input("Enter True or False for value A: ").strip().lower() == "true"
b = input("Enter True or False for value B: ").strip().lower() == "true"

print(f"A and B = {a and b}")   # True only if BOTH are True
print(f"A or B  = {a or b}")    # True if AT LEAST ONE is True
print(f"not A   = {not a}")     # Flips the boolean

# --- BITWISE OPERATORS ---
x = 5   # binary: 0101
y = 3   # binary: 0011

print(f"\nx = {x} ({bin(x)}), y = {y} ({bin(y)})")
print(f"x & y  (AND) = {x & y} ({bin(x & y)})")    # 1 only where BOTH bits are 1
print(f"x | y  (OR)  = {x | y} ({bin(x | y)})")     # 1 where EITHER bit is 1
print(f"x ^ y  (XOR) = {x ^ y} ({bin(x ^ y)})")     # 1 where bits DIFFER
print(f"~x     (NOT) = {~x} ({bin(~x)})")           # flips all bits, result is -(x+1)
print(f"x << 1 (LEFT SHIFT)  = {x << 1} ({bin(x << 1)})")   # shifts bits left, doubles value
print(f"x >> 1 (RIGHT SHIFT) = {x >> 1} ({bin(x >> 1)})")   # shifts bits right, halves value