import random

# Initialize variables
guess = 0
attempt = 0
# Generate a random secret number between 1 and 100
secret = random.randint(1, 100)

# Display instructions to the user
print("I am a very smart computer and I have a secret number!")
print("You have 6 attempts to guess it! The guessed number is in the range from 1 to 100")
print()

# Start the guessing loop
while guess != secret and attempt < 6:
    # Get user input for their guess
    guess = int(input("Your attempt: "))

    # Check if the guess is less than the secret number
    if guess < secret:
        # Provide feedback to the user and display remaining attempts
        print("This is less than the secret number! (you have {} attempts left):".format(abs(attempt - 5)))
    # Check if the guess is greater than the secret number
    elif guess > secret:
        # Provide feedback to the user and display remaining attempts
        print("This is more than the secret number! (you have {} attempts left):".format(abs(attempt - 5)))
    
    # Increment the attempt counter
    attempt += 1

print("\n")

# Check if the user guessed the secret number
if guess == secret:
    # Display a congratulatory message
    print("You are awesome! You guessed it! Congratulations!")
else:
    # Display a message indicating the end of attempts and reveal the secret number
    print("The attempts are over. Better luck next time!")
    print("The secret number was: ", secret)
