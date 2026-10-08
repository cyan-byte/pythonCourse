# =================  My Contact Book App (M*A*D*E W*I*T*H P*Y*T*Y*O*N)  ===================

# This is my dictionary of original contacts.
contact_book = {
    "Alisha": "555-1234",
    "My Mama": "555-5678",
    "BFF": "555-9101",
    "Sister IC": "555-1121",
    "Brother IC": "555-3141",
    "Spam": "555-8000"
}
# ========================  Add Contact  =========================

# These variables allow my user to enter a name and a phone number.
# contact_name = input("Name: ")
# contact_phone = input("Phone: ")

# def add_contact():
#     contact_book[f"{contact_name}"] = f"{contact_phone}"

# # Don't forget to CALL the function so that this contact book machine can actually work :)
# add_contact()

# print(contact_book)


# ========================  View Contacts  =========================
# My user is able to view all contacts with this function
# def view_contacts():
#     # it means for every name and phone number in the contact book, print each one to the screen
#     for key, value in contact_book.items():
#         print(f"{key} {value}")

# view_contacts()


# ========================  Find Contact  =========================
# This function allows my user to type in a name and search for it
# find_contact = input("Enter a name to search for: ")

# def search_contacts():
#     for key, value in contact_book.items():
#         if key == find_contact:
#             print(f"{key} {value}")
# search_contacts()


# ========================  Delete Contact  =========================
# Too many calls from this suspicious company I have saved. 
# Time to delete it.
# User enters a name to search for
delete_a_contact = input("Which entry do you want to delete? ")

def delete_contact():
    # and if it is in the contact book, it's getting deleted (as long as it passes the try net...)
    if delete_a_contact in contact_book:
        # If the name is found, it deletes the entry
        try:
            del contact_book[delete_a_contact]
            
            # I consider this line good UX writing. It tells you the entry is deleted, stating back its name (no confusion)
            print(f"{delete_a_contact} is deleted.")
        # Not found? Try again.    
        except:
            print("Try again")
    # If the user enters something not found in the contact book, there's an error message:
    else:
        print(f"I did not find \"{delete_a_contact}\" in your contacts. Is it spelled correctly?")
delete_contact()
print(contact_book)
