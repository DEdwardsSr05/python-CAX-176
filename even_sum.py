# David Edwards
# 2026-CAX-176
# July 21, 2026
# ALAB 353.3
# even_sum.py

# even_sum.py
# Calculates the sum of even numbers from 1 to 50 using both a for loop and a while loop

# --- FOR LOOP VERSION ---
total_for = 0
for num in range(1, 51):   # range(1, 51) covers 1 through 50 inclusive
    if num % 2 == 0:        # % is modulo — checks if there's no remainder when divided by 2 (i.e. even)
        total_for += num    # augmented assignment: total_for = total_for + num

print(f"The sum of even numbers from 1 to 50 is {total_for}.")

# --- WHILE LOOP VERSION ---
total_while = 0
n = 1
while n <= 50:
    if n % 2 == 0:
        total_while += n
    n += 1   # manual increment — for loops handle this automatically, while loops don't

print(f"The sum of even numbers from 1 to 50 is {total_while}.")

# Both loops produce the same result (650) because they check the exact same condition
# (n % 2 == 0) over the exact same range (1-50). The for loop is cleaner here since
# range() already handles the start/stop/increment for us — the while loop needs that
# logic written out manually (n = 1, then n += 1 each pass).