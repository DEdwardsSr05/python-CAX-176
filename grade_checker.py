# David Edwards
# 2026-CAX-176
# July 21, 2026
# ALAB 353.3
# grade_checker.py

# grade_checker.py
# Takes a numeric grade (0-100) and converts it to a letter grade using if/elif/else

grade = int(input("Enter your numeric grade (0-100): "))

# Guard clause: Catch invalid input BEFORE running the grade logic.
# Anything outside 0-100 isn't a real grade, so we stop here instead of
# letting it fall through and get mislabeled as an A.
if grade < 0 or grade > 100:
    print("Invalid grade entered. Please enter a number between 0 and 100.")
else:
    # Check ranges from highest to lowest — order matters here.
    # Once one condition is True, the rest are skipped (that's what elif does).
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    else:
        letter = "F"

    print(f"Your grade is: {letter}")

    # Conditional expression (ternary) — one-line if/else that returns a value
    # Reads as: value_if_true if condition else value_if_false
    message = "Congratulations, you passed!" if letter in ("A", "B", "C") else "Keep trying, you can improve!"
    print(message)