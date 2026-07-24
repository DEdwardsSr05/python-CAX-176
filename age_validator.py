# David Edwards
# 2026-CAX-176
# July 24, 2026
# ALAB 356.2 - Task 3: Custom exception test (Age validator)

"""
Goal: this is your first real exposure to RAISING your own exception,
rather than just catching exceptions Python throws at you (ValueError,
IndexError, etc. that already exist naturally, like in list_manager.py).

Key idea: `raise` lets YOUR code decide something is an error, even
though Python itself wouldn't complain. Python has no problem with the
number 200 - it's a perfectly valid int. But 200 isn't a valid human
age, so WE define that rule ourselves and force an error to happen
on purpose when it's broken.
"""


def validate_age(age):
    """Check whether age is a valid human age (0-120 inclusive).
    Raises ValueError if not. Returns nothing if the age is fine -
    the function's whole job is to complain, not to hand back a value."""

    # <= and >= together check the age is inside the 0-120 window.
    # If age is NEGATIVE or OVER 120, this condition is True, and we
    # deliberately trigger an exception ourselves with `raise`.
    if age < 0 or age > 120:
        raise ValueError(f"Age {age} is not valid. Must be between 0 and 120.")

    # If we get here, age was fine - the function just ends normally,
    # no exception, no return value needed.


# --- Main script ---
raw_age = input("Enter your age: ")

try:
    # int() first - this can ALSO raise its own ValueError if the user
    # types something non-numeric like "twelve". That's a different
    # ValueError than the one validate_age() raises on purpose, but
    # Python doesn't care - both get caught by the same except block
    # below since they're the same exception TYPE.
    age = int(raw_age)

    # Now hand it to our custom function. If age is out of range,
    # validate_age() raises ValueError here, which immediately jumps
    # down to the except block - none of the code after this line runs.
    validate_age(age)

    # This only prints if BOTH int() and validate_age() succeeded
    # without raising anything.
    print(f"Age {age} is accepted.")

except ValueError as error:
    # `as error` captures the exception object so we can print its message.
    # This one except block handles BOTH possible ValueErrors above:
    # the int() conversion failure and our own validate_age() raise.
    print(f"Invalid input: {error}")
