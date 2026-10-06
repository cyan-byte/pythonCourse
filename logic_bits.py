# This function will run my request for a Boolean user input.
def get_user_response1():
    user_response1 = input("Is the sky blue? (Y/N)")
    # This compares the user's input to "Y" or "N"
    if user_response1.upper() == "Y":
        user_result1 = True
        # This converts the user's Boolean respons to base-2 binary
        print(f"True. {bin(user_result1)}")
        # Because the user result equates to True, which is 0b1 or 1,
        # it gets a 1 when compared to the & operator which needs both bits to be 1
        # 0b1
        # 0b1
        # ^^ place them in the bitmasking binary columns and you get two 1s in the 1 row, meaning "True"
        if user_result1 & 0b1:
            print("You get normal blue skies.")
        
    elif user_response1.upper() == "N":
        user_result1 = False
        # This converts the user's Boolean respons to base-2 binary
        print(f"False. {bin(user_result1)}")
    else:
        print("Try again.")
        get_user_response1()

get_user_response1()

# The following function does a similar job as the preceding one. See comments.
def get_user_response2():
    user_response2 = input("Is the sky green? (Y/N)")
    if user_response2.upper() == "N":
        user_result2 = True
        print(f"True. {bin(user_result2)}")
        if user_result2 | 0b1:
            print("You get strange zombie-looking skies.")
    elif user_response2.upper() == "Y":
        user_result2 = False
        print(f"False. {bin(user_result2)}")
    else:
        print("Try again.")
get_user_response2()
  
