# ======================  NUMBER 1  ===============================

# 1.) I start off by defining my function using "def"
def greet_user():
    # The Function's Instructions:
    # Next, I need to store the user's input to use it later in my printed string:
    first_name = input("Enter your name: ")
    # Since I want to give the actual greeting, I'll use the user's above input:
    print(f"Hello, {first_name}! Welcome!")

# Put the function's instructions to work:
# This is what we call "calling" the function
greet_user()

# =====================  NUMBER 2  =================================

# 2.) Get the Sum of Two Numbers:
# Define the function, and let it return the sum of two numbers a and b.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

def add_two_numbers(a, b):
    total = int(a + b)
    print(f"{a} + {b} = {total}")
    if a + b == total:
        return True
    else:
        return False
print(a + b)

answer = add_two_numbers(a, b)

print(f"This answer is {answer}.")


# ====================  NUMBER 3  ==================================

# 3.) Define a function is_even(num) that returns True if num is even or False otherwise
# I want user input, so I need to capture that input outside of the function:

user_number = int(input("Enter a number: "))
# Then pass that input variable into the function as an argument
def is_even(user_number):
    # if the number the user enters is even,
    if user_number % 2 == 0:
        # Save it as True in the background
        return True
    # if the number the user enters is odd,
    else:
        # Save it as True in the background
        return False
# Now I need to save the result of the function to a variable (named "result"). My result is a Boolean value
result = is_even(user_number)
# If the user types 8, this will print: "Is 8 even? True"
print(f"Is {user_number} even? {result}")

