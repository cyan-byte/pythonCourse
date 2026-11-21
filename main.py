# Import syntax: from filename_without_py import Item1, Item2
from todo_list import load_tasks, save_tasks, add_task, list_tasks, complete_task, delete_task

def run_app():
    # Issue:
    #      I had while True: above load_tasks() at first, but that would cause the tasks to be loaded on every turn of the loop
    load_tasks()
    while True:
        # Displays the available menu optoins to the console
        print("\n*** To-Do List Menu ***")
        print("(A) Add a new task ")
        print("(C) Mark a task as completed ")
        print("(D) Delete a task ")
        print("(L) List all tasks ")
        print("(Q) Quit ")
        # Takes the user input and removes any leading/trailing spaces and makes the input lowercase
        menu_choice = input("Choose an option (A, C, D, L, or Q): ").strip().lower()
        # Checks the user's menu choice
        if menu_choice == "a":
            add_task()
        elif menu_choice == "c":
            complete_task()
        elif menu_choice == "d":
            delete_task()
        elif menu_choice == "l":
            list_tasks()
        elif menu_choice == "q":
            # Issue: At first, I didn't have save_tasks here, so nothing was actually being saved to my TASKS_FILE
            save_tasks()
            print("Have a nice day.")
            # break ends the loop and ends the program
            break
        else:
            print("Invalid menu letter.")
if __name__ == "__main__":
    run_app()