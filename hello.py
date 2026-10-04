print("Hello, World!", "Welcome to Python programming.", sep="\n")
user_name = input("What is your name?: ")
allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789"
if user_name == "":
    print("I didn't get your name. Please try again.")
elif any(char not in allowed_characters for char in user_name):
    print("Invalid name. Please use only letters, numbers, and/or underscores.")
else:
    print(f"Hello, {user_name}! Glad to have you learning Python.")
