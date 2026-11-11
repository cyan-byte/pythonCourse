# Script Welcome Message:
print("=========================== Managing a List of Numbers ===========================")
# I start with a list of numbers (integers)
int_list = [5, 10, 15, 20, 25]
allowed_numbers = "0123456789"

# The user's number input is converted to an integer
add_a_number = int(input("Add a number to the list: "))
# This adds/appends the number to the end of the list
int_list.append(add_a_number)
int_list.pop(3)  # This removes the number at index 3

def run_app():
    while True:
        print("    ~ List of Numbers ~    ")
        print("(a) Add a number to the list")
        print("(b) Remove a number from the list")
        print("(c) Display numbers from the list")
        print("(d) Quit: Exit the program")

if __name__ == "__main__":
    run_app()