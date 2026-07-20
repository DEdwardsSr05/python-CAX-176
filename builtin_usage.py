# David Edwards
# 2026-CAX-176
# July 20, 2026
# ALAB 356.1 - Modules, Packages and PIP


import math       # gives us math functions like sqrt() and floor()
import random      # gives us random.randint() for random numbers
import platform    # gives us OS/version info about the machine running the script

# Generate a random integer between 1 and 100 (inclusive on both ends)
num = random.randint(1, 100)

# math.sqrt() always returns a float, even if the result is a whole number
sqrt_result = math.sqrt(num)

# math.floor() rounds a float DOWN to the nearest int (not the same as round())
floored_sqrt = math.floor(sqrt_result)

# platform.system() returns the OS name, e.g. 'Windows', 'Linux', 'Darwin' (Mac)
os_name = platform.system()

# platform.python_version() returns the interpreter version as a string, e.g. '3.12.4'
py_version = platform.python_version()

# Descriptive print statements — labels make output readable, not just raw values
print("Random Number:", num)
print("Square Root (floored):", floored_sqrt)
print("Operating System:", os_name)
print("Python Version:", py_version)