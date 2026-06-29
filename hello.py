# This is a Python program that prints a greeting message and asks for the user's name.
# David Edwards
# 2026-CAX-176

# Introduction
print("Hello, World!")
print("Welcome to Python programming.")

# Ask for the user's name
name = input("What is your name? ")
if name == "":
	name = "stranger"
	
# Greet the user
print("Hello, " + name + "! Glad to have you learning Python.")