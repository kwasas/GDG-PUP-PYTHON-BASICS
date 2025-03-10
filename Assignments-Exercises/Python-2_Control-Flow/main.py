error1 = "Invalid input: Age cannot be a non-number."
error2 = "Invalid input: Age cannot be negative."

try:
    # Get user input
    user_input = int(input("Please enter your age: "))

    # Check the age category
    if user_input < 0:
        raise ValueError(error2)
    elif user_input < 13:
        print("You are categorized as: Child")
    elif user_input < 20:
        print("You are categorized as: Teenager")
    elif user_input < 60:
        print("You are categorized as: Adult")
    else:
        print("You are categorized as: Senior")
        
except ValueError:
    print(error1)
