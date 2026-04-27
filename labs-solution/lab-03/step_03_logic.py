# Step 3: Getting and Checking the User's Guess
# This demonstrates the core game logic inside the loop

import random

# Generate a random secret channel number
secret_channel = random.randint(1, 50)

# For debugging - remove this in the final game
print(f"Secret number was: {secret_channel}")

# Print welcome message
print("Welcome to the BBC Channel Guessing Game!")
print("I'm thinking of a channel number between 1 and 50.")
print("You have 5 tries to guess it!")

attempt = 0
number_of_guesses = 5
while attempt < number_of_guesses:
    print(f"\nAttempt {attempt + 1} of 5")
    
    # Get the player's guess
    guess = int(input("Enter your guess (1-50): "))
    if guess < 1 or guess > 50:
        print("Out of range, try again.")
        continue 
    # Check the guess
    if guess == secret_channel:
        print("🎉 Congratulations! You've guessed correctly!")
        print(f"The secret channel was {secret_channel}!")
        break  # Exit the loop early
    elif guess < secret_channel:
        print("📺 Too low! Try a higher channel number.")
    else:
        print("📺 Too high! Try a lower channel number.")
    
    # Show remaining attempts
    remaining = 5 - (attempt + 1)
    if remaining > 0:
        print(f"You have {remaining} attempt(s) remaining.")   

    attempt = attempt + 1 # attempt += 1
 




# Create the game loop with guessing logic
for attempt in range(5):
    print(f"\nAttempt {attempt + 1} of 5")
    
    # Get the player's guess
    guess = int(input("Enter your guess (1-50): "))
    
    # Check the guess
    if guess == secret_channel:
        print("🎉 Congratulations! You've guessed correctly!")
        print(f"The secret channel was {secret_channel}!")
        break  # Exit the loop early
    elif guess < secret_channel:
        print("📺 Too low! Try a higher channel number.")
    else:
        print("📺 Too high! Try a lower channel number.")
    
    # Show remaining attempts
    remaining = 5 - (attempt + 1)
    if remaining > 0:
        print(f"You have {remaining} attempt(s) remaining.")

print("\nGame finished!")


