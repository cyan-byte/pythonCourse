# The user inputs a sentence
sentence = input("Enter a quick sentence: ")
# This is where we find out what a vowel is
vowels = "aeiouAEIOU"
# This begins the count of the vowels at 0
count = 0
# This converts the entire sentence to uppercase letters & prints the result
print(f"Uppercase: {sentence.upper()}")
# This reverses the inputted sentence & prints the result
# The -1 walks through the string backwards
print(f"Reversed: {sentence[::-1]}")

# Now we step through each letter in the sentence to find each vowel
for letter in sentence:
    if letter in vowels:
        print(f"{letter} is a vowel.")
        # This keeps count of each vowel from the inputted sentence
        count += 1
print(f"Vowel count: {count}")

print(f"Modified string: {sentence.replace(' ', '-')}")