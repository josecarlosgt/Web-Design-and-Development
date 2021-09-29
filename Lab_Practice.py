## LAB PRACTICE: Python Basics

# Implement a game where the user tries to guess a number between 1 and 20.
#
# Your program must generate a random number between 1 and 20.
# The user should get cues on whether their guesses are too high or too low.
#
# Tip: Use a while loop.

# Import the randint function from the random module
from random import randint

# Generate a random number between 1 and 20
random = randint(1, 20)
print(random)

# YOUR SOLUTION HERE

# Recommended steps:

# Create a boolean variable named guessing with value True

# Create a while statement that runs while guessing is True
  
    # Ask a number to the user using the function input() and assign the value to a variable called number

    # Convert the number variable into an integer using the function int()
    
    # Write a conditional statement that checks if the user number is greater or less than the random number
        # If the user number is greater, display the message "Number is too high!"
        # If the user number is less, display the message "Number is too low!"
        # If both numbers are equal:
             # Display the message "You won!"
             # Assign False to the guessing variable
