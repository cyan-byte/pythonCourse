# Note: I'm aware this architecture is not the recommended structure, so I'm actively studying best practices for my future Python scripts.

# =================  My Contact Book App (M-A-D-E  W-I-T-H  P-Y-T-Y-O-N)  ===================

# This is my dictionary of original contacts.
contact_book = {
    "Alisha": "555-1234",
    "My Mama": "555-5678",
    "BFF": "555-9101",
    "Sister IC": "555-1121",
    "Brother IC": "555-3141",
    "Spam": "555-8000"
}

def run_app():
    while True:
        print("~ 📱 CONTACT BOOK MENU 📱 ~\n  🔸1. Add New Contact\n  🔸2. View All Contacts\n  🔸3. Search Contact\n  🔸4. Delete Contact\n  🔸5. Exit")
        menu_choice = input("Enter a menu number (1-5): ")
    # ======================================================================

        if menu_choice == "1":
        # ========================  Add a New Contact  =========================

        # Challenges: At first, I did not set up the function to take parameters,
        # so I moved the input variables to the inside of the function PARAMETERS
        # and deleted the input() lines from inside the function body
            def add_contact(contact_name, contact_phone):
        # if the input name is already listed in my contact_book dictionary, display an error message.
                if contact_name in contact_book:
                    print("Error: This is a possible duplicate entry. Contact not saved.")
        # If it DOES NOT match a name already in my contact_book, it's okay to add it.
                else:
                    # This is simply the syntax of adding an entry to a dictionary
                    contact_book[contact_name] = contact_phone
                    print(f"{contact_name} is now saved to your Contacts.")

        # Don't forget to CALL the function so that this contact book machine can actually work :)
        # I learned that the inputs should be placed below the function so taht Python has the function fully registered before user execution
        # These variables allow my user to enter a name and a phone number.
            contact_name = input("Name: ")
            contact_phone = input("Phone: ")

            add_contact(contact_name, contact_phone)

            print(contact_book)


        # ========================  View All Contacts  =========================
                
        elif menu_choice == "2":
        # My user is able to view all contacts with this function
            def view_contacts():
        # it means for every name and phone number in the contact book, print each one to the screen
        # It's best practicce to use a top-level if/else to verify (first) that any data exists at all, then move onto loop checking.
                if len(contact_book) == 0:
                    print("Contact list is empty.")
                else:
                    # This is the simple syntax for looping through keys and values at the same time
                    for key, value in contact_book.items():
                        print(key, value)

            view_contacts()

# =========================  Search for a Contact  =========================  
        # If user chooses menu option 3, she/he will be taken to the search contacts part of the app
        elif menu_choice == "3":

        #This function allows my user to type in a name and search for it
            # It takes the user input which is the variable "user_query"    
            def search_contacts(user_query):
                # to weed out confusion, I used the .lower() string operation with dot notation to change the input to all lowercase.
                lower_cased_query = user_query.lower()
                # This means, search through the contact name and phone in contact book
                for contact_name, contact_phone in contact_book.items():
                    # and if you find this user input (which was turned into lowercase characters)
                    if lower_cased_query in contact_name.lower():
                        # display the name and phone number of that found entry
                        print(f"{contact_name} {contact_phone}")
            # This prompts the user to enter a name (or part of a name)
            user_query = input("Enter a name to search for: ")
            search_contacts(user_query)


# ========================  Delete Contact  =========================
        elif menu_choice == "4":

        # "Hmm... Getting too many calls from this suspicious company I have saved. 
        # Time to delete it."
        # User enters a name to search for

            def delete_contact(delete_a_contact):
                # and if it is in the contact book, it's getting deleted (as long as it passes the try net...)
                if delete_a_contact in contact_book:
                    # If the name is found, it deletes the entry
                    try:
                        del contact_book[delete_a_contact]
                        
# I consider this line good UX writing. It tells the user the entry is deleted, stating back its name (no confusion)
                        print(f"{delete_a_contact} is deleted.")
                    # Not found? Try again.    
                    except:
                        print("Try again")
                # If the user enters something not found in the contact book, there's an error message:
                else:
                    print(f"I did not find \"{delete_a_contact}\" in your contacts. Is it spelled correctly?")

            # This is the argument that the function takes at execution
            delete_a_contact = input("Which entry do you want to delete? ")
            # This line deletes the entry
            delete_contact(delete_a_contact)
            # and this one shows the evidence of deletion by reloading the remaining contacts
            print(contact_book)
            # This is the final menu choice, which exits the app with a farewell and a break statement.
        elif menu_choice == "5":
            print("Goodbye!")
            break
            
# This checks if this script is the script being called before it runs the function    
if __name__ == "__main__":
    # This runs the app and loads the main menu with the initial prompt to enter a menu number.
    run_app()