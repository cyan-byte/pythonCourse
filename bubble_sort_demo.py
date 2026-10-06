# Create a messy list
house_number_list = [8841, 72, 29, 1822]

# Find the number of items inside the list.
list_amount = len(house_number_list) # equals 4

# Count the total number of attempts, (not the list index positions like the inner loop does.
for all_loop_turns in range(list_amount): # makes sure the inner loop gets to check through the full list each time (not just part of it), so we use list_amount here (since we NEEED to know how many items are in the list in the first place)

# Grab the item at index i (current index), and check if it is larger than its neighbor immediately to its right (index i + 1)
    for index in range(list_amount - 1):
        if house_number_list[index] > house_number_list[index + 1]:

# If the item on the left is bigger than the item on the right, do the tuple unpacking swap to flip their positions
            house_number_list[index], house_number_list[index + 1] = house_number_list[index + 1], house_number_list[index]
print(house_number_list)











# ===========================================================
#                       MORE PRACTICE
# ===========================================================

# # Create a messy list
# ages = [97, 102, 94, 88]
# # Find the number of items inside the list.
# number_of_ages = len(ages)
# # Count the total number of attempts, (not the list index positions like the inner loop does. This is the inner loop, btw: for i in range(length - 1)
# # makes sure the inner loop gets to check through the full list each time (not just part of it), so we use list_amount here (since we NEEED to know how many items are in the list in the first place)
# for each_full_check in range(number_of_ages):

# # Look at the whole list again (minus 1) and grab the item at index i (current index), and check if it is larger than its neighbor immediately to its right (index i + 1)
#     for each_full_check in range(number_of_ages - 1):

# # If the item on the left is bigger than the item on the right, do the tuple unpacking swap to flip their positions
#         if ages[each_full_check] > ages[each_full_check + 1]:
#            ages[each_full_check], ages[each_full_check + 1] = ages[each_full_check + 1],ages[each_full_check]  
# # Print the results
# print(ages)

# ===============================================================
#                        PRACTICE AGAIN
# ===============================================================
# Create a messy list

# Find the number of items inside the list.

# Count the total number of attempts, (not the list index positions like the inner loop does.

# makes sure the inner loop gets to check through the full list each time (not just part of it), so we use list_amount here (since we NEEED to know how many items are in the list in the first place)

# Look at the whole list again (minus 1) and grab the item at index i (current index), and check if it is larger than its neighbor immediately to its right (index i + 1)

# If the item on the left is bigger than the item on the right, do the tuple unpacking swap to flip their positions

# Print the results

# ========================================================

#           More Practice with Years of Birth

# =======================================================
# # Create a messy list
# year_of_birth = [1862, 1981, 1492, 1776]
# # Find the number of items inside the list.
# number_of_birth_years = len(year_of_birth)
# # Count the total number of attempts, (not the list index positions like the inner loop does. This is the inner loop, btw: for i in range(length - 1)
# # makes sure the inner loop gets to check through the full list each time (not just part of it), so we use list_amount here (since we NEEED to know how many items are in the list in the first place)
# for each_year in range(number_of_birth_years):
# # Look at the whole list again (minus 1) and grab the item at index i (current index), and check if it is larger than its neighbor immediately to its right (index i + 1)
#     for index in range(number_of_birth_years - 1):
# # If the item on the left (use the name of the list) is bigger than the item on the right, do the tuple unpacking swap to flip their positions
#         if year_of_birth[index] > year_of_birth[index + 1]:
#             year_of_birth[index], year_of_birth[index + 1] = year_of_birth[index + 1], year_of_birth[index]

# # Print the results
# print(year_of_birth)