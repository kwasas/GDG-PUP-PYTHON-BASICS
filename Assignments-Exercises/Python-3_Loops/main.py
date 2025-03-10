favorite_foods = ['Burger', 'Fried Chicken', 'Pares', 'Grilled Pork', 'Rice Cake']

print('My favorite foods:')
# Print each food item
for food in favorite_foods:
    print(f"- {food}")  

print('\n')

# Ask user input
num = input("Please enter a positive integer: ").strip()

try:
    # Try to convert input to an integer
    num = int(num)
    
    # Check if the number is positive
    if num > 0:
        print("Countdown:")
        while num > 0:
            print(num)
            num -= 1
        print("Countdown complete!")
    else:
        print('Invalid input: Please enter a positive integer.')

except ValueError:
    # Catches if input is not a valid integer
    print("Invalid input: Please enter a valid integer.")
