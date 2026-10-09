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


# # Challenges: At first, I did not set up the function to take parameters,
# # so I moved the input variables to the inside of the function PARAMETERS
# # and deleted the input() lines from inside the function body
# def add_contact(contact_name, contact_phone):
#         # if the input name is already listed in my contact_book dictionary, display an error message.
#         if contact_name in contact_book:
#             print("Error: This is a possible duplicate entry. Contact not saved.")
#         # If it DOES NOT match a name already in my contact_book, it's okay to add it.
#         else:
#             # This is simply the syntax of adding an entry to a dictionary
#             contact_book[contact_name] = contact_phone
#             print(f"{contact_name} is now saved to your Contacts.")

# # Don't forget to CALL the function so that this contact book machine can actually work :)
# # I learned that the inputs should be placed below the function so taht Python has the function fully registered before user execution
# # These variables allow my user to enter a name and a phone number.
# contact_name = input("Name: ")
# contact_phone = input("Phone: ")

# add_contact(contact_name, contact_phone)

# print(contact_book)




# ========================  View Contacts  =========================
# My user is able to view all contacts with this function
# def view_contacts():
#     # it means for every name and phone number in the contact book, print each one to the screen
#         # It's best practicce to use a top-level if/else to verify (first) that any data exists at all, then move onto loop checking.
#         if len(contact_book) == 0:
#             print("Contact list is empty.")
#         else:
#             # This is the simple syntax for looping through keys and values at the same time
#             for key, value in contact_book.items():
#                 print(key, value)

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
# delete_a_contact = input("Which entry do you want to delete? ")

# def delete_contact():
#     # and if it is in the contact book, it's getting deleted (as long as it passes the try net...)
#     if delete_a_contact in contact_book:
#         # If the name is found, it deletes the entry
#         try:
#             del contact_book[delete_a_contact]
            
#             # I consider this line good UX writing. It tells you the entry is deleted, stating back its name (no confusion)
#             print(f"{delete_a_contact} is deleted.")
#         # Not found? Try again.    
#         except:
#             print("Try again")
#     # If the user enters something not found in the contact book, there's an error message:
#     else:
#         print(f"I did not find \"{delete_a_contact}\" in your contacts. Is it spelled correctly?")
# delete_contact()
# print(contact_book)
