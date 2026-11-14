
def gen_fibonacci(n):
    # current_number might be a better name
    zero = 0
    # next_number might be a better name
    one = 1
    # This underscore variable is what Python allows if you don't want to USE the variable,
    # but only want the loop to repeat for the range(n), for example.
    # Basically, it's a loop variable I don't need
    for _ in range(n):
        # "yield" makes this function a "generator" not a regular function (Python turns functions into generators when they hit "yield")
        # yield sends "zero" to the program & pauses the fn.
        yield zero

        # the function pauses after getting this yield zero instruction and saves the current spot in the range() loop,
        # instead of shutting down the function like "return" does and starting over the next time it's called

        # *** ISSUE *** At first, I had one + 1, not zero + one and it only added 1 to each number instead of the Fibonacci sequence...
        # But each new Fibonacci number is the sum of the two previous variables
        # current number, next number = next number, current number plus next number
        zero, one = one, zero + one

# This simply checks if the current file is the current "main" file. If so, it executes the following blocks
if __name__ == "__main__":
    print("Running local generator tests...")
    # This is the "n" for the gen_fibonacci() function where the user inputs a number
    n = int(input("Enter how many numbers you want for the Fibonacci sequence: "))

# For each number in the user input number of the Fibonacci generator, print this string along with the current number in the sequence
    for num in gen_fibonacci(n):
        print(f"Fibonacci number: {num}")