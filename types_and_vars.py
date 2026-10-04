# This takes variables and places them into an f-string to be inserted into a sentence.
# age_in_five_years adds 5+ years to the age variable.
name = "Alisha"
age = 72
height = 1.7
age_in_five_years = age + 5
print(f"Hello, my name is {name} and I\'m {age} years old and {height} meters tall. In five years, I will be {age_in_five_years} years old.")

# Here's a simple area calculator built into a string.
rectangle_width = 5.5
rectangle_height = 2
print(f"The area of a 5.5 x 2 rectangle is {rectangle_width * rectangle_height}.")

# This script finds out if your house number is odd or even.
# This uses the % and * operators, along with string concatenation
house_number = (int(input("Enter your house number: ")))
result = "Your house number is"

if house_number % 2 != 0:
    print(f"{result} odd" + "!"*3)
else:
    print(f"{result} even" + "!"*3)