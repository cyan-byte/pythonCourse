# ============== Script Welcome Message ==============
print("=========================== 🔢 Managing a List of Numbers 🔢 ===========================")
# I start with a list of numbers (integers)
int_list = [5, 10, 15, 20, 25]
allowed_numbers = "0123456789"
menu_validation = ["a", "b", "c", "d"]

# ============== Functions ==============
# (a)
def add_number():
    # The user's number input is converted to an integer
    add_a_number = int(input("Add a number to the list: "))
    # This adds/appends the number to the end of the list
    int_list.append(add_a_number)
    print(f"\033[92m {add_a_number} has been added to the list.\033[0m")
    print(f"Updated list: {int_list}")

# (b)
def remove_number():
    try:
        # This removes the number at the chosen index
        user_index = int(input("Enter an INDEX to remove: "))
        # This takes the user input and stores it in "removed_number"
        removed_number = int_list.pop(user_index)
        # This only prints the number that was removed
        print(f"\033[92m {removed_number} has been removed.\033[0m")
        # Here's the updated list after the number was removed
        print(f"\033[92m Updated list: {int_list}\033[0m")
    # This throws an error if the inputted index is not found
    except IndexError:
        print(f"\033[91m **** Error: Index not found in this list. ****\033[0m")

# (c)
def display_list():
    # This shows us the current state of the list
    print(f"\033[92m Current list: {int_list}\033[0m")

# (d)
# This exits the program if the user chooses option (d) from the menu
def quit_app():
    print("Goodbye!")

# ============== User Input ==============

def run_app():
    # While the app is running...
    while True:
        # Display this menu:
        print("    ~ List of Numbers ~    ")
        print("(a) Add a number to the list")
        print("(b) Remove a number from the list")
        print("(c) Display numbers from the list")
        print("(d) Quit: Exit the program")
        # This prompts the user to select a menu option and converts it to lowercase for simple validation
        user_selection = input("Select a Menu Option: ").lower()
        # if what the user selects is in the menu_validation list (above)...,
        if user_selection.lower() in menu_validation and user_selection.isalpha():
            # ... try this. This tells you what happens if the user selects each option from the menu
            try:
                if user_selection == "a":
                    add_number()
                elif user_selection == "b":
                    remove_number()
                elif user_selection == "c":
                    display_list()
                elif user_selection == "d":
                    quit_app()
                    break
        # if the user selects something invalid, they'll get an error message in red:
            except ValueError:
                print("\033[91m**** Invalid selection. Please try again. ****\033[0m")
        else:
            print("\033[91m**** Invalid menu option. Please enter a, b, c, or d. ****\033[0m")


# ============== Application Launch ==============
if __name__ == "__main__":
    run_app()