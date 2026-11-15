# I'm only importing the date module from datetime
from datetime import date

# The user's input is saved as year and month variables
year = int(input("Enter a year (YYYY): "))
month = int(input("Enter a month (MM): "))

# This gives us today's date
date_for_today = date.today()
# And this is the formatted date where %B = the full month name, %d = the day of the month, and %Y = the 4-digit year.
formatted_date = date.fromisoformat(f"{date_for_today}").strftime("%B %d, %Y")

# If the user enters today's date...
if date_for_today.year == year and date_for_today.month == month:
    # They'll get a clear statment on today's date
    print(f"Today is {formatted_date}")
else:
    # If they enter a different date, they'll be told that it's not today's date.
    print(f"The date you entered is NOT {formatted_date}")
    
# ✅ Prompts the user for a year and a month (e.g., 2025 and 3 for March 2025).
# ✅ Uses the calendar module to display the calendar for that month in a neatly formatted grid.
# ✅ Uses the datetime module to determine today’s date.
# ✅ If today’s date falls in the specified month and year, prints a message indicating so (e.g., “Today is March 4, 2025”) or highlights the day in the output.
# ✅ Clearly labels all outputs for readability.