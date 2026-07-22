# David Edwards
# 2026-CAX-176
# July 21, 2026
# ALAB 353.4
# data_processing.py
# Simulates processing course grade data, including an empty-data edge case

def get_average_grade(grades_tuple):
    # Guard against dividing by zero if the tuple is empty
    try:
        return sum(grades_tuple) / len(grades_tuple)
    except ZeroDivisionError:
        return None   # signals "no data" to the caller instead of crashing

# Dictionary where each course maps to a tuple of grades.
# History is intentionally empty to test the edge case.
course_grades = {
    "Math": (85, 90, 78, 92),
    "Science": (88, 95, 91),
    "History": ()   # edge case: no grades recorded yet
}

for course, grades in course_grades.items():
    average = get_average_grade(grades)
    if average is None:
        print(f"No grades available for {course}.")
    else:
        print(f"The average grade for {course} is {average:.1f}")