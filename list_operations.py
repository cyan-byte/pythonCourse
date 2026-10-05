# Original list:
# Creates a list of 5 random integers called "numbers"
numbers = [100, 40, 2, 17, 1]
print(numbers)

# ====================================================

#Sorted List:
# This sorted() function sorts the numbers without changing the original list
print(sorted(numbers))
# This proves that index 0 is still 100
print(numbers[0])

# ====================================================

# Appended list:
# Adds the number 50 to the end of the numbers list
numbers.append(50)
print(numbers)

# ====================================================
# Deleted element in list:
# Delete an element from the numbers list. I'll delete [3]. That will now make [4] equal 50 
del numbers[3]
print(numbers)

# ====================================================

# Reversed list:
# Arranges the list in reverse order
numbers.reverse()
print(numbers)
