# Lab 351.2
# David Edwards
# 2026-CAX-176

# Declare a variable "name" and assign my name as a string.
name = 'King Jaffe Joffer'

# Declare a variable "age" and assign my age as an integer.
age = 51

# Declare a variable "height" and assign my height in meters as a float.
# Convert the height from inches.
height_in_inches = 76
height = float(height_in_inches / 39.3701)

# Introduction
print('Hello my name is ' + name + '. I am ' + str(age) + ' years of age and my height is ' + str(round(height, 2)) + ' meters.')

#Add 5 years to my age and print the age in the future
age_in_5_years = age + 5
print('In 5 years I will be ' + str(age_in_5_years) + ' years old.')

#Calculate the area of a rectangle with the width of 5.5 meters and height of 2 meters. Print the area.
width = 5.5
length_of_rectangle = 2
area = width * length_of_rectangle
print('I am trying to figure out the the area of a rectangle for my garden. The width is ' + str(width) + ' meters and the length is ' + str(length_of_rectangle) + ' meters. This is small for a garden, but its a start.')
print('The area is ' + str(area) + ' m^2.')