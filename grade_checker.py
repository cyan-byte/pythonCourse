# User enters their grade as a number
grade = input("Enter your numeric grade (from 0-100): ")
grade = int(grade)

while True:
    if grade < 0 or grade > 100:
        print("Error *** Please enter a valid grade between 0 and 100. ***")
        grade = input("Enter your numeric grade (from 0-100): ")
        grade = int(grade)
    else:
        break

def grade_message(letter):
    if letter == "A":
        return "Congratulations! You're doing great!"
    elif letter == "B":
        return "Great job! I can see your effort!"
    elif letter == "C":
        return "You're getting there, but I believe you can do better!"
    elif letter == "D":
        return "Don't give up. I advise you to come to tutoring."
    elif letter == "F":
        return "The truth is, you're not ready and need help with grasping the concepts. Come to tutoring."

if grade >= 90:
    print("Your letter grade is: A")
    print(grade_message("A"))
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
