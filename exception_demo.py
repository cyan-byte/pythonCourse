# My function allows you to safely divide any two numbers (as long as they're actually... numbers)
# This safe_divide() function lets you type in two numbers (when you call it)
def safe_divide(a,b):
    # The script attempts to divide a by b
    try:
        a = float(a)
        b = float(b)

        division = a/b
        # if successful, it prints the results of a/b
        print(division)
    # But if there's an issue with trying to divide by zero...    
    except ZeroDivisionError:
        print("Triggered a ZeroDivisionError. Dividing by zero is mathematically impossible.")
    # or an issue with trying to do math with a n
    except ValueError:
        print("Triggered a ValueError. I accept strings here, but only number strings.")
    # or an issue with trying to do math with data types that cannot physically do math together
    except TypeError:
        print("Triggered a TypeError. I cannot do math between numbers and incompatible data types")
    # But then there's this catch-all except block that catches all system errors simultaneously
    
    # COMMENT OUT THE ERROR(S) ABOVE TO SEE THIS except Exception WORK.
    except Exception as error_message:
        print(f"This is a the actual system error: {error_message}")
    
    finally:
        print("Division operation completed (whether or not an error occured).")
safe_divide(20, list[8])