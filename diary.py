# ================= PURPLE DIARY ===================
# The os module lets my script verify whether certain files exist on my computer's hard drive
import os
# 'datetime' lets me generate real-time timestamps for the diary entries
import datetime
# This global constant (ALL CAPS) points to the file name I need in my current directory
# Because this new file is going to be in the same folder as my script, I can just use a relative file name (no path)
DIARY_FILE = "diary.txt"
# This function checks if DIARY_FILE 
def initialize_diary():
    # If the file doesn't exist, this line creates it
    if not os.path.exists(DIARY_FILE):
        # try-except here around the disc operations (open, etc.) catches errors to avoid a crash
        try:
            with open(DIARY_FILE, mode="w", encoding="utf-8") as file:
                # 'pass' tells Python to 'do nothing' since I don't want to write any text into an already-created file
                pass # 'pass' is a placeholder since Python requires 'something' to be added here
        # This triggers if the try fails (OS or hard drive error)    
        except OSError as e:
            # The actual error prints here
            print(f"Error: {e}")
# Now I get to add an entry            
def add_entry(entry_text):
    # This variable adds a real-time timestamp to diary entries
    timestamp = datetime.datetime.now()
    # Now a try-except block to prevent crashing
    try:
        # Opens the diary.txt file in append mode to add new entries below previous ones (without overwriting them)
        with open(DIARY_FILE, mode="a", encoding="utf-8") as file:
            # This allows me to write something
            # It's similar to a print() statement, except it sends text right into the file I've chosen (diary.txt) instead of sending it to the console
            # file.write() doesn't automatically add '\n'
            # and it only accepts a single text string
            file.write(f"[{timestamp}] {entry_text}\n")
    # Catches any potential OS errors
    except OSError as e:
        print(f"Error: {e}")

# This function's job is to read and print all of diary.txt so the user can see all of the past entires
def read_all_entries():
    # Try opening the diary file only to read it (read-only mode)
    try:
        with open(DIARY_FILE, mode="r", encoding="utf-8") as file:
            # file.read() takes no arguments
            # 'file' is the open file object created by with open(DIARY_FILE,...)
            # print is wrapped around the file.read() function so I can read the full file
            print(file.read().strip())
    # More error-catching
    except OSError as e:
        print(f"Error: {e}")

# If this is the file being directly run, execute this block
if __name__ == "__main__":
    # Calls the initialize_diary() function to see if diary.txt exists... if not, it creates it
    initialize_diary()
    # This is where the user gets to start writing
    user_entry = input("Enter your diary entry: ")
    # Adds the user's diary entry to the file in append mode with a timestamp from the imported datetime module
    add_entry(user_entry) # the user's entry MUST be passed inside the parentheses here
    # This final function reads and prints all diary entries to the console
    read_all_entries()