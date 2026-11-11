# This function checks if the age a user enters is valid
def validate_age(age):
    # First, it tries to accept the number...
    try:
        # Converts the age to an integer and stores it as "numeric_age"
        numeric_age = int(age)
        # Checks if it's within range.
        # Python evaluates both of these conditions at once (is 0 less than or equal to numeric age AND less than or equal to 120?)
        if 0 <= numeric_age <= 120:
            print("\033[92m Age IS accepted.\033[0m")
        # But if the number is OUTSIDE of the age range...
        else:
            # ... it prints the following error message:
            print("\033[91m Age NOT accepted. \033[0m")
    except ValueError:
        # Python catches the error instead of crashing the program
        print("\033[91m *** Error: Invalid age. ***\033[0m")
# The user enters an age
user_input = input("Enter your age: ")
# The entered age gets validated
validate_age(user_input)