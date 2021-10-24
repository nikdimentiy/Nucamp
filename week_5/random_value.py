import random


guess = 0
attempt = 0
secret = random.randint(1, 100)
print("I am a very smart computer and I have a secret  number!")
print("You have 6 attempts - to guess it! The guessed number in the range from 1 to 100")
print()
while guess != secret and attempt < 6:
    guess = int(input("Your attempt: "))
    if guess < secret:
        print("This is less than planned number! ""(you have {} attempts left):".format(abs(attempt - 5)))
    elif guess > secret:
        print("This is more than planned number! ""(you have {} attempts left):".format(abs(attempt - 5)))
    attempt += 1
print("\n")
if guess == secret:
    print("You are awesome! You guessed it! Congratulations!")
else:
    print("The attempts are over. You will be lucky next time!")
    print("The secret number is: ", secret)
