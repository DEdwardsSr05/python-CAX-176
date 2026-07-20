# David Edwards
# 2026-CAX-176
# July 20, 2026
# ALAB 356.1 - Modules, Packages and PIP
# utilities.py

import math   # we'll use math.factorial() instead of writing our own loop

def greet(name):
    # f-string builds a greeting using the name passed in
    return f"Hello, {name}! Welcome."

def factorial(n):
    # math.factorial() does the multiplication for us (n! = n*(n-1)*...*1)
    return math.factorial(n)