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