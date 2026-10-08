# This function calcuates the average of any grades entered into the tuple. It even handles the ZeroDivisionError
def get_average_grade(grades_tuple = (87, 90, 95, 95)):
    # This keeps track of the grades
    grades_sum = 0
    # This counts the number of items in the tuple. It starts at zero and increases with every outer loop
    count = 0

    # This shows the loop where to look (look at each grade in the grades_tuple)
    for grade in grades_tuple:
        # This adds each singular grade to the grades sum, one by one (90 + 95 + 95 + 87)
        # grades_sum starts at 0, then each time it moves to the next grade, it adds that next grade to the current grades_sum
        grades_sum += grade
        # This allows me to count the number of times the loop goes through the singular grades (4 times). I need this to calculate the average.
        count += 1
    # Here's where my program will try to get the average, if it can't because the count is zero,    
    try:
        average = grades_sum / count
        return average
    # It triggers the built-in ZeroDivisionError and prints an error statement
    except ZeroDivisionError:
        print("No grades found. Try again.")
        return None

# Here, I get to make the function work and see the results, using one line
print(get_average_grade())