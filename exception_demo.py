# David Edwards
# 2026-CAX-176
# July 21, 2026
# ALAB 353.4
# exception_demo.py
# Demonstrates raising a custom ValueError, try/except/finally, and catching a generic Exception

def safe_divide(a, b):
    if b == 0:
        # raise lets YOU trigger an exception on purpose, instead of waiting for Python to do it
        raise ValueError("Cannot divide by zero")
    return a / b

# --- Test safe_divide with a zero divisor ---
try:
    result = safe_divide(10, 0)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error: {e}")
finally:
    # finally ALWAYS runs, whether an exception happened or not — good for cleanup messages
    print("Division operation completed.")

# --- Test safe_divide with a valid divisor, for comparison ---
try:
    result = safe_divide(10, 2)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("Division operation completed.")

# --- Generic exception demo: invalid string-to-int conversion ---
try:
    number = int("not_a_number")
except Exception as e:
    # Catching the general Exception class catches any error type,
    # useful when you're not sure exactly what might go wrong
    print(f"An error occurred: {e}")