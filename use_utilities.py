# Here, I'm pulling the greet(), the_factorial(), first_name, and n functions from the utilities.py file in the mypackage folder
from mypackage.utilities import greet, the_factorial, first_name, n
# This prints the greeting message from utilities.py and the factorial of the number that the user inputs
print(greet(first_name))
print(the_factorial(n))