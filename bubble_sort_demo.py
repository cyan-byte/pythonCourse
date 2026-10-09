# Create a messy list
house_number_list = [8841, 72, 29, 1822]

# Find the number of items inside the list.
list_amount = len(house_number_list) # equals 4

# Outer Loop: Count the total number of attempts, (not the list index positions like the inner loop does.
# Step 1: Where are we looking?:
for all_loop_turns in range(list_amount): # OUTER LOOP'S JOB: it only sits in the background, counting the total number of complete laps.
    # This makes sure the inner loop gets to check through the full list each time (not just part of it). We use list_amount here (since we NEEED to know how many items are in the list in the first place)
    # On the first turn of the loop, the index sits at 0, waiting for the inner loop to finish walking the entire list from begining to end before it clicks over to index 1

# Grab the item at index i (current index), and check if it is larger than its neighbor immediately to its right (index i + 1)
# So first, we find out where we're looking:
# The next line means "Walk down the list item-by-item, but stop exactly one slot before the very last item"
# This range can also be saved into a variable, by the way.
    for index in range(list_amount - 1): # INNER LOOP'S JOB: Step through each index number (one by one), using those index numbers to compare and swap the side-by-side items in teh list. Once it reaches the end of its index range, it stops, waits for the outerloop teo move to the next turn, and then resets back to index 0 to start counting down the list all over again. <------ THIS!
        if house_number_list[index] > house_number_list[index + 1]:

# If the item on the left is bigger than the item on the right, do the tuple-unpacking-swap to flip their positions
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

#           More Practice
#              Try Again with Years of Birth

# =======================================================
# # Create a messy list
# year_of_birth = [1862, 1981, 1492, 1776]
# # Find the number of items inside the list.
# number_of_birth_years = len(year_of_birth)
# # Count the total number of attempts, (not the list index positions like the inner loop does.

# # makes sure the inner loop gets to check through the full list each time (not just part of it), so we use list_amount here (since we NEEED to know how many items are in the list in the first place)
# for each_year in range(number_of_birth_years):
# # Look at the whole list again (minus 1) and grab the item at index i (current index), and check if it is larger than its neighbor immediately to its right (index i + 1)
#     for index in range(number_of_birth_years - 1):
# # If the item on the left (use the name of the list) is bigger than the item on the right, do the tuple unpacking swap to flip their positions
#         if year_of_birth[index] > year_of_birth[index + 1]:
#             year_of_birth[index], year_of_birth[index + 1] = year_of_birth[index + 1], year_of_birth[index]

# # Print the results
# print(year_of_birth)