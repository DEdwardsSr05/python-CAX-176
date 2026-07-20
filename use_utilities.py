# David Edwards
# 2026-CAX-176
# July 20, 2026
# ALAB 356.1 - Modules, Packages and PIP
# use_utilities.py

from mypackage import utilities  # imports the utilities module from inside the mypackage package

# call greet(), passing a name string
greeting = utilities.greet("David")
print(greeting)

# call factorial(), passing an integer
result = utilities.factorial(5)
print("Factorial of 5:", result)