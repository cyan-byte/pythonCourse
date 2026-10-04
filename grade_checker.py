# User enters their grade as a number
grade = input("Enter your numeric grade (from 0-100): ")
grade = int(grade)

# This means: For the entire time that the grade number is less than 0 or greater than 100, print an error and prompt user to reenter number
while True:
    # Is the grad within our range or not? Hmm... This checks it for you:
    if grade < 0 or grade > 100:
        print("Error *** Please enter a valid grade between 0 and 100. ***")
        grade = input("Enter your numeric grade (from 0-100): ")
        # grade gets converted back to an integer each time the loop has to loop due to an error
        grade = int(grade)
    # If it does not produce the preceding error, stop the loop and continue to the rest of the code    
    else:
        break
# This is my function that checks which letter grade the user currently has and displays a message on the status of the grade
def grade_message(letter):
    # Got an A?
    if letter == "A":
        # Wow, congrats! etc.
        return "Congratulations! You're doing great!"
    elif letter == "B":
        return "Great job! I can see your effort!"
    elif letter == "C":
        return "You're getting there, but I believe you can do better!"
    elif letter == "D":
        return "Don't give up. I advise you to come to tutoring."
    elif letter == "F":
        return "The truth is, you're not ready and need help with grasping the concepts. Come to tutoring."
    
# This checks which letter grade to assign to a particular range of numerical grades

# Got a 90 or greater? (Up to 100, of course because of our previous checks)
if grade >= 90:
    print("Your letter grade is: A")
    print(grade_message("A"))
# Got a B? Etc...
elif grade >= 80:
    print("Your letter grade is: B")
    print(grade_message("B"))
elif grade >= 70:
    print("Your letter grade is: C")
    print(grade_message("C"))
elif grade >= 60:
    print("Your letter grade is: D")
    print(grade_message("D"))
else:
    print("Your letter grade is: F")
    print(grade_message("F"))
