# This is the outer function returns an inner function
def make_multiplier(factor):
    # This is the actual tool being used to multiply
    def multiply(x):
        # It returns the argument times the input below
        return factor * x
    # This is the step that returns the whole inner function
    return multiply

# These variables multiply the factor by the input (ex. 5 * 3) 
times3 = make_multiplier(int(input(f"Enter a number: ")))
# (ex. 5 * 10)
times10 = make_multiplier(int(input(f"Enter a second number: ")))
# This is the output of the multiplier closure with 3 and 10 as examples.
print(f"5 * 3 = {times3(3)}")
print(f"5 * 10 = {times10(10)}")