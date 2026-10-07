# This function is a calculator. It can take a user input and calculate using an operation input (+=*/)
# The function's name is "calculate"
def calculate():
    # First, I need to make sure I set up a variable for later that can check if the user uses the right operations
    allowed_operations = "+-*/"
    # While it's true that the user's input is a number
    # If it is a number, the input gets converted into a float
    while True:
        try:
            a = input("Enter the first number: ")
            a = float(a)
            break
        except:
        # It the input is NOT a number, it prints an error and the loop goes back to asking the user to enter the first number
            print("Error *** Invalid input. Please enter numbers only. ***")
    # Another "while check". This one checks if the user entered a proper operation
    # If what the user entered is NOT in the allowed_operations variable, an error message displays and it loops back up to "Choose an op..."
    # This check doesn't need a try/except because it doesn't cause a system-level crash
    while True:
        op = input("Choose an operation (+, -, *, /): ")
        if op not in allowed_operations:
            print("Error. Please choose either +, -, *, or /.")
        # Once the user enters one of the allowed operations, this loop breaks (stops looping back up to "Choose an operation:")
        else:
            break

    # This is the same check as the one on the above "a" variable to make sure the variable works with float() 
    # This way,it doesn't remain a string (because we can't do math on strings)
    while True:
        try:
            b = input("Enter the second number: ")
            b = float(b)
            break
        except:            
            print("Error *** Invalid input. Please enter numbers only. ***")

    # Now we get to do the actual work of calculating the user's numbers
    # Here, I'm setting up my addition sub-function along with the other sub-functions
    def add():
        return f"{a} + {b} = {a + b}"
    def subtract():
        return f"{a} - {b} = {a - b}"
    def multiply():
        return f"{a} * {b} = {a * b}"
    # This block is special because if user enters a number divided by zero, it will cause a ZeroDivisionError
    # So I need to be ready for that:
    def divide():
        # This function needs to have the ZeroDivisionError exception handled.
        # How? It will try to complete 5 / 0, for example, then once the computer chip hits that mathematical wall,
        # It will jump down to the except part of the code and return this text: "Error. Division by zero is not allowed."
        # If it's any other number, it will just do the division from "try"
        try:
            return f"{a} / {b} = {a / b}"
        except ZeroDivisionError:
            return "Error. Division by zero is not allowed."
    
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
