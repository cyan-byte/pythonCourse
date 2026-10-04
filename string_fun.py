# The function completes 3 tasks: 1) It counts the number of letters in the word, 2) It converts the word to uppercase, and 3) It repeats the word 3 times.
def string_fun():
    # User enters a word through the input() function.
    word = input("Enter a word: ")
    # This converts any lowercase letters in {word} to uppercase letters.
    uppercase_word = word.upper()
    word_three = f"{word * 3}" # Use the f-string to repeat the word 3 times. The multiplier goes inside the curly braces.
    print(len(word))
    print(uppercase_word)
    print(word_three)

string_fun() # Calls the function to perform the tasks and display the results.