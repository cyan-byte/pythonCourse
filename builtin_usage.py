# These import the modules I need to use the following script
from random import randint
from platform import python_version, system
from math import sqrt, floor


# This will choose a random integer between 1 and 100
random_integer = randint(1, 100)
# Then it calculates the square root of the random integer
square_root = sqrt(random_integer)
# Finally, it rounds the rounded number using floor division
rounded_integer = floor(square_root)

# These statements print the results of the functions, the Windows system information, and the Python version
print(f"Random integer is: {random_integer}")
print(f"Square root of the random integer is: {square_root}")
print(f"Floored square root is: {rounded_integer}")
print(f"Operating system is: {system()}")
print(f"Python version is: {python_version()}")
