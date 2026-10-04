# year = int(input("Enter the year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("That's a leap year!")
# else:
#     print("That's a common year!")

# if year < 1582:
#     print("Not within the Gregorian calendar period.")

#==================================================================================
# birth_year = int(input("Enter your birth year: "))
# current_year = int(input("Enter the current year: "))
# age = current_year - birth_year

# print("This year, you turned (or will turn): ", age)

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# height =

# print(f"")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# operation = input("Choose an operation (+, -, *, /): ")

# if operation == "+":
#     print(num1 + num2)
# if operation == "-":
#     print(num1 - num2)
# if operation == "*":
#     print(num1 * num2)
# if operation == "/":
#     print(num1 / num2)

# Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
# x = 1
# while x < 11:
#     if x % 2 == 1:
#         print(x)
#     x += 1

# n = 0
# while n != 3:
#     print(n)
#     n += 1
# else:
#     print(n,"else")
# print()

# for i in range(0, 3):
#     print(i)
# else:
#     print(i, "else")

# x = 5
# print(not (x > 3 and x < 10))

# variable = 17
# variable_right = variable >> 1
# variable_left = variable << 2
# print(variable, variable_left, variable_right)

# for ch in "jane.smith@python.org":
#     if ch == "@":
#         break
#     print(ch, end="")

# var = 1
# print(var > 0)
# print(not (var <= 0))
# print(var != 0)
# print(not (var == 0))

# list = [0,1,2,3]
# for z in list:
#     print(z)
# else:
#     print(z, "else")

# def hello(name): # defining a function
#     print(f"Hello, {name}.") # body of function

# hello("Alisha") # calls the hello()

# def hi_all(name_1, name_2):
#     print("Hi,", name_2)
#     print("Hi,", name_1)

# hi_all("Sebastian", "Konrad")

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name) # This is what the introduction() function does when called.
# introduction("Shelly", "Smith") # give the function the arguments it needs to run (a first name and a last name).
# # try:
# #     introduction("Shelly") # This will cause an error because the function expects two arguments
# introduction("Asland", "Lion") # This will work because the function is given the correct number of arguments

numbers = [10, 5, 7, 2, 1]
print(numbers)

numbers [0] = 111 # Changes the value of index 0 in the list to 111
print(numbers)

numbers [1] = numbers [4] # Changes the value of index 1 in the list to the value of index 4 (same value)
print(numbers)

