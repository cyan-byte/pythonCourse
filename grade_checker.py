# User enters their grade as a number
grade = input("Enter your numeric grade (from 0-100): ")
grade = int(grade)
allowed_grades = grade > 0 or grade < 100

while True:
    if grade < 0 or grade > 100:
        print("Error *** Please enter a valid grade between 0 and 100. ***")
        grade = input("Enter your numeric grade (from 0-100): ")
        grade = int(grade)
    else:
        break
if grade >= 90:
    print("Your letter grade is: A")
elif grade >= 80:
    print("Your letter grade is: B")
elif grade >= 70:
    print("Your letter grade is: C")
elif grade >= 60:
    print("Your letter grade is: D")
else:
    print("Your letter grade is: F")
