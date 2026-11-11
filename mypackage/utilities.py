# First, I get the factorial function from the math module
from math import factorial
# Next, I create a function that greets the user by name
def greet(name):
    return f"Welcome, {name}."
# This does the factorial conversion of the number that the user inputs
def the_factorial(n):
    return factorial(n)
# Here are the actual input statements that the functions use
first_name = input("Enter your first name: ")
n = int(input("Enter a number: "))
