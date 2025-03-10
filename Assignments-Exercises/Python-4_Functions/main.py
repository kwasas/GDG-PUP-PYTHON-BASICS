# Greeting function1
def create_greeting(name):
    return f"Hello {name}! Welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"

# Main program
name = input("What is your name?: ").strip()

if name.isalpha():
    # Display the greeting message
    greeting = create_greeting(name)
    print(f"\n{greeting}")
else:
    print("Invalid input: Please enter a valid name.")

