# TASK: GET THE SUM OF ALL EVEN NUMBERS FROM 1 - 50.
# =================================================================
# We start with i equaling zero
i = 0
# This variable will store what i is at the turn of each loop in the for loop below
# The For Version (I like this one better):
even_sum1 = 0
# This means, every time we iterate over the numbers 1 - 50, if the numbers are even, we're adding the current "number i" to even_sum.
# So on the first loop, i
for i in range(1,51):
    if i % 2 == 0:
        print(i)
        even_sum1 += i

print(f"For loop result: {even_sum1}")

# ============================================================================================================

# The While Version of this:
# Since I plan to use range(1,51), j will start with 1 (the first number in my range [instead of zero])
j = 1
even_sum2 = 0
while j in range(1,51):
# While there's an even number between 1 and 50:
    if j % 2 == 0:
        even_sum2 += j
        print(j)
    j += 1 # Increment each turn by 1 so the loop counts up to 50 (range(1,51))

print(f"While loop result: {even_sum2}")