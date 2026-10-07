# This function is a calculator. It can take a user input and calculate using an operation input (+=*/)
# The function's name is "calculate"
def calculate():
    # First, I need to make sure I set up a variable for later that can check if the user uses the right operations
    allowed_operations = "+-*/"
    # While it's true that the user's input is a number
    # If it is a number, the input gets converted into a float
    while True:
        a = input("Enter the first number: ")
        if a.replace(".", "").isdigit():
              a = float(a)
            # The "while checking" stops (using "break") to move onto the next line of code.
              break
        # It the input is NOT a number, it prints an error and the loop goes back to asking the user to enter the first number
        print("Error *** Invalid input. Please enter numbers only. ***")
    # Another "while check". This one checks if the user entered a proper operation
    # If what the user entered is NOT in the allowed_operations variable, an error message displays and it loops back up to "Choose an op..."
    while True:
        op = input("Choose an operation (+, -, *, /): ")
        if op not in allowed_operations:
            print("Error. Please choose either +, -, *, or /.")
        # Once the user enters one of the allowed operations, this loop breaks (stops looping back up to "Choose an operation:")
        else:
            break
    # This is the same check as the one on the above "a" variable to make sure the second number is first a digit, then converts that digit into a float (so it doesn't remain a string [We can't do math on strings...])
    while True:
        b = input("Enter the second number: ")
        if b.replace(".", "").isdigit():
              b = float(b)
              break
        
        print("Error *** Invalid input. Please enter numbers only. ***")
    # Now we get to do the actual work of calculating the user's numbers
    # Here, I'm setting up my addition sub-function along with the other sub-functions
    def add():
        return f"{a} + {b} = {a + b}"
    def subtract():
                return f"{a} - {b} = {a - b}"
    def multiply():
                return f"{a} * {b} = {a * b}"
    def divide():
                return f"{a} / {b} = {a / b}"
    # Now, at the same indentation as the sub-functions, I check what operation the user chose earlier and if it's "+", that means addition.
    if op == "+":
            # At first, I had the function calls within the sub-functions
            # adding this at the bottom of the op checks is the right order
            # If the operation is chosen, it prints the results of that operation's function
            print(add())
    elif op == "-":
            print(subtract())
    elif op == "*":
            print(multiply())
    elif op == "/":
            print(divide())
# This finally calls the full calculate function so that it can do the calculations.
calculate()
