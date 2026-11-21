import os
# This line looks into the task.py file and imports the Task class
from task import Task

# Save tasks.txt to a constant variable using ALL CAPS
TASKS_FILE = "tasks.txt"

# This empty list is global and it's a blank slate for me to add every task
tasks = []

# This function saves the file so Python doesn't wipe it clean after the user quits the program
def save_tasks():
    # This line is aligned with the try block in this function, so as soon as the user enters his/her input, the try-except block gets to work
    save_file = input("Do you want to save your tasks file? (Y/N) ")
    try:
        if save_file.strip().lower() == "y":
            # This line is how the file actually gets saved
            # Python must first open (or unlock) the file using open()
            with open(TASKS_FILE, mode="w",encoding="utf-8") as file: # "file" is a temporary variable. It gets used in the next line of code.
                # When Python is finished with the "with open()" line, it closes the temporary "file" and saves teh task to the hard drive
                # Check each line in the tasks.txt file
                for task in tasks:
                    # Save the task and its status
                    file.write(f"{task.title},{task.completed}\n")
    # This catches any operating system error and prints the exact error
    except OSError as e:
        print(f"Error: {e}")
   
# This runs once when the program starts to get previously saved tasks
def load_tasks():
    # If the file doesn't exist ...
    if not os.path.exists(TASKS_FILE):
        # ... end the load_tasks() function now.
        return
    # try to open the file in read-only mode
    try:
        # This opens tasks.txt in read-only mode, since I only want to see the tasks
        with open(TASKS_FILE, mode="r", encoding="utf-8") as file:
            # This reads each line in the TASKS_FILE
            for line in file:
                # This skips blank lines and loads lines that actually contain a task
                if line.strip():
                    title, completed_str = line.strip().split(",")
                    # This converts text to a boolean
                    completed = completed_str == "True"
                    # This works from the inside out; calls the Task class's __init__ to build a new Task object using the title string and completed boolean ^^^
                    tasks.append(Task(title, completed)) # this takes the new Task object (Task(title, completed [starts as false even if I don't add the completed parameter)) and adds it to the end of my tasks list

# Note: I wondered why this append() function was needed in the load_tasks() function. The reason is that Task objects disappear when I close the program, but on startup, load_tasks() reads tasks.txt and rebuilds them back into working Task objects again.
                    
    # This will print one of these exact system errors
    except (OSError, ValueError) as e:
        print(f"Error: {e}")

def add_task():
    # The user types in a task and .strip() removes any extra spaces at the beginning or end of the task string and saves it into a variable named "title".
    title = input("Enter a task: ").strip()
    # This checks if the user actually typed something (to make it truthy)
    if title:
        # The user's task gets added to the Task object and saved to the end of the tasks[] list
        tasks.append(Task(title))
        print("Task added.")
    # This handles blank inputs because title must be truthy to add it to the tasks list.
    else:
        print("Task cannot be empty.")

# This is for the "List Tasks" menu option
def list_tasks():
    # If the tasks list is empty...
    if not tasks:
        print("List is empty: ")
        return
    # enumerate gives us the task and its index: first the counter (i), then the {task}. start=1 changes the default start=0 to start=1 (counts from 1 instead of 0).
    for i, task in enumerate(tasks, start=1):
        print(f"{i} {task}") # prints the index first, then the task b/c of the order I put them in the f-string (print controls the display order here)

# This method marks tasks as complete
def complete_task():
    if not tasks:
        print("Tasks list is empty.")
        # Ends the complete_task() function
        return
    # Shows the user the whole list of saved tasks first
    list_tasks()
    # Error handling for negative numbers or numbers outside the number of tasks in the list
    try:
        task_number = int(input("Enter the number of the task you want marked as complete: ")) - 1
        # This means if 0 is less than or equal to task_number input (after subtracting 1), perform the next line. It's looking for 0+
        if 0 <= task_number < len(tasks):
            # This takes the tasks list, uses the user's task number input as the index to find (-1) and marks it complete by attaching task_complete() and calling on it
            tasks[task_number].task_complete()
        else:
            print("Enter a valid number.")
    # Catches any ValueError system error
    except ValueError as e:
        print(f"{e} Enter numbers only.")

def delete_task():
    if not tasks:
        print("Task list is empty.")
        return
    list_tasks()
    try:
        # Takes user's numerical input and converts it into an integer
        deleted_task = int(input("Which task number do you want to delete? ")) -1
        # Shows the full list of saved tasks
        if 0 <= deleted_task < len(tasks):
            # This takes the tasks list, used the user's input as the index (-1) and deletes that task
            # Issue: I had this at first:
            # "tasks[deleted_task].pop(tasks)" here at first. That would call .pop() on a Task object instead of the tasks list
            # This is what it should be:
            removed_task = tasks.pop(deleted_task)
            # .pop() calls on the tasks list
            # This allows the user to see just which task was deleted
            print(f"Deleted: {removed_task}")
        else:
            # The input is out of range and throws an error print statemetn
            print("Enter a valid number. ")
    except ValueError as e:
        print(f"{e}: Enter numbers only.")

