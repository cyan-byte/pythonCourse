# 1) First, I need the input variables. This allows the user to type the first number.
first_number = input("Enter your first number: ")

# 2) Next, Operation Validation. Did the user enter +, -, *, or /?
allowed_operations = "+-*/"
# Keeps the user in a loop until he/she enters a valid operation. Anything typed here is constantly checked. If allowed, the loop breaks.
while True:
    chosen_operation = input("Choose an operation (+, -, *, or /): ")    
# If what the user chose is not part of the allowed operations (+ - * /), try again.
    if chosen_operation not in allowed_operations:
        print("Error *** Please only choose from +, -, *, or /.***")
    else:
        break # Loop finally breaks. The user is freed from the loop once a valid operation is chosen.

# 3) Now the user is able to type the second number.
second_number = input("Enter your second number: ")

# 4) Next, the input validation for the numbers.
# NOTE: isdigit() is a string method; it only works on strings and breaks on numbers.
# .replace() removes any decimal points before checking if the numbers are digit (using isdigit()).
if not first_number.replace(".", "").isdigit():
    print("Error *** Invalid input. Please enter numbers only. ***")
else:
    first_number = float(first_number)
    second_number = float(second_number)
    
# Now the calculations can be performed since the numbers are actual numbers.
    addition = f"{first_number} + {second_number} = {first_number + second_number}"
    subtraction = f"{first_number} - {second_number} = {first_number - second_number}"
    multiplication = f"{first_number} * {second_number} = {first_number * second_number}"
    division = f"{first_number} / {second_number} = {first_number / second_number}"

# 5) Finally, the function that performs the calculation and gives us the answer.
def perform_operation():
    if chosen_operation == "+":
        return addition
    elif chosen_operation == "-":
        return subtraction
    elif chosen_operation == "*":
        return multiplication
    elif chosen_operation == "/":
        return division
    else:
        print("Error *** Please enter a valid operation. ***")

print(perform_operation()) # Calls the function to perform the operation and display the answer.
