# ================================ Tuples =====================================

# Here, I created a tuple (they're like lists, but are IMMUTABLE and use parentheses)
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November,", "December")
# I want to get the first month (index 0)
print(months[0])
# and the last month (index -1 [or index 11])
# print() allows me to acutally SEE the data
print(months[-1])

# My change_month function will attempt (try) to change the first month to "Earth"
def change_month():
    try:
        months[0] = "Earth"
# But it hits a TypeError. (At first, I tried SyntaxError here, but it's not that type of error. The syntax was already correct)
    except TypeError:
# if the try fails, it drops down to this except block to tell the me that "... tuples are immutable."
        return "Error. Did you forget that tuples are immutable?"
print(change_month())

# ================================== Dictionaries =====================================

# This is my "students" dictionary made of name keys and grade values for each student
students = {
    "Juliet": 87,
    "Android": 90,
    "Paul": 95
}

# This adds a new student to my "students" dictionary: Her name is Shell and her grade is 92.
students["Shell"] = 92

# This prints the contents of the full current dictionary
print(students)

# But wait, I need to update Shell's grade because she turned in extra credit
students["Shell"] = 95

# This prints the updated list
print(students)

# I want to loop through the grades instead, and have the key-value pairs print out in a formatted way:
for student, grade in students.items():
    print(f"{student}'s grade is {grade}")