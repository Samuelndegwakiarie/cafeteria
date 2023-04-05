# Define a function to greet the customer
def greet_customer():
    print("Welcome to the cafeteria!")
    print("What's your name?")

# Define a function to display the menu
def display_menu():
    print("Here's our menu:")
    print("1. Tea")
    print("2. Black coffee")
    print("3. White coffee")

# Call the greet_customer function to greet the customer
greet_customer()

# Get the customer's name
name = input()

# Display the menu
display_menu()

# Ask the customer to choose a drink
drink = input("Please choose a drink (enter 1, 2, or 3): ")

# Process the customer's choice
if drink == '1':
    print(f"Great choice, {name}! Enjoy your tea.")
elif drink == '2':
    print(f"Great choice, {name}! Enjoy your black coffee.")
elif drink == '3':
    print(f"Great choice, {name}! Enjoy your white coffee.")
else:
    print("Sorry, we don't have that drink on the menu.")

# Ask the customer to rate their experience
rating = input(f"How was your experience, {name}? Please rate us on a scale of 1 to 10: ")

# Convert the rating to an integer
rating = int(rating)

# Check the rating and provide feedback
if rating < 5:
    print("We're sorry to hear that you didn't enjoy your experience. We'll do our best to improve.")
elif rating < 8:
    print("Thank you for your feedback. We're always looking to improve our service.")
else:
    print("Wow, a perfect 10! Thank you for your business and we hope to see you again soon!")
