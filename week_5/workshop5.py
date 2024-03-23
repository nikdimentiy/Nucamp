import random

def guess_random_number(tries, start, stop):
    """
    This function allows the user to guess a random number within a specified range.

    Args:
        tries (int): The number of attempts allowed.
        start (int): The starting value of the range.
        stop (int): The ending value of the range.

    Returns:
        None
    """
    number = random.randint(start, stop)
    past_guess = []

    while tries != 0:
        print("🔥 Number of tries left: 🔥", tries)

        # Input validation loop for user guesses
        while True:
            guess = input(f"Guess a number between {start} and {stop}: ")

            if not guess.isnumeric() or not (int(guess) >= start and int(guess) <= stop):
                print(f"Please enter ONLY numbers between {start} and {stop}.")
            elif guess in past_guess:
                print(f"You already guessed number {guess}. Please try again.")
            else:
                past_guess.append(guess)
                break

        # Check if the guess is correct
        if int(guess) == number:
            print("🌹🌹🌹 YES! It's the correct answer! 🌹🌹🌹")
            return
        elif int(guess) < number:
            print("Guess higher! 🔺")
        else:
            print("Guess lower! 🔻")
        
        tries -= 1

    # If all tries are used up
    print("You've used all your tries. ❌❌❌ You failed. ❌❌❌")
    print(f"The guess number is {number} 🌼!")


def guess_random_num_linear(tries, start, stop):
    """
    This function performs linear search to guess a random number within a specified range.

    Args:
        tries (int): The number of attempts allowed.
        start (int): The starting value of the range.
        stop (int): The ending value of the range.

    Returns:
        bool: True if the number is guessed, False otherwise.
    """
    number = random.randint(start, stop)
    print("The number for the program to guess is 🍀:", number)

    for i in range(start, stop + 1):
        print("Number of tries left: 📡", tries)
        print("------------------------------")
        print("The program is guessing...", i)
        if i == number:
            print("👌 🌼🌼🌼 The program has guessed the correct number! 🌼🌼🌼 👌")
            return True
        else:
            tries -= 1
            if tries == 0:
                print("❌❌❌ The program has failed to guess the correct number. ❌❌❌")
                return False


def guess_random_num_binary(tries, start, stop):
    """
    This function performs binary search to guess a random number within a specified range.

    Args:
        tries (int): The number of attempts allowed.
        start (int): The starting value of the range.
        stop (int): The ending value of the range.

    Returns:
        None
    """
    number = random.randint(start, stop)
    print("Random number to find: 🍀", number)

    while start <= stop:
        pivot = (start + stop) // 2
        if pivot == number:
            print("🟩🟩🟩 Found it! 🟩🟩🟩", number)
            return
        if pivot > number:
            stop = pivot - 1
            print("🔻 Guessing lower!")
        else:
            start = pivot + 1
            print("Guessing higher! 🔺")
        tries -= 1
        if tries == 0:
            print("❌❌❌ Your program failed to find the number. ❌❌❌")
            return


def guess_menu():
    """
    This function displays a menu for the user to choose a guessing method.
    """
    tries = int(input("\n🔰 Enter number of tries 🔰: "))
    start = int(input("Enter start value: "))
    stop = int(input("Enter end value: "))

    while True:
        method = input(
            "\nPress 1 to guess manually\n"
            "Press 2 to search linearly\n"
            "Press 3 to perform binary search\n"
            "Press 'Q' to quit: ").lower()
        if method.isnumeric():
            if method == '1':
                guess_random_number(tries, start, stop)
                continue
            elif method == '2':
                guess_random_num_linear(tries, start, stop)
                continue
            elif method == '3':
                guess_random_num_binary(tries, start, stop)
                continue
        elif method == 'q':
            break
        else:
            print("\nWrong Input! Try Again.")


def gambling_mode():
    """
    This function simulates a gambling mode where the user bets on the computer's guessing outcome.
    """
    player_money = 10

    while True:
        print("\nYour balance is: 💲", player_money)
        print("✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
        call = input(
            "\nEnter 'Y' to bet that the computer WILL guess the correct number\n"
            "Enter 'N' to bet that the computer WILL NOT guess the correct number\n"
            "------------------------------------------------------------------\n"
            "Your prediction (Y/N): ").lower()
        bet = input("How many dollars will you bet? Enter 1 to 10: ")

        if bet.isnumeric():
            result = guess_random_num_linear(5, 0, 10)
            if (result and call == 'y') or (not result and call == 'n'):
                player_money += int(bet)
                print("💸 You won! You now have 💰", player_money)
            else:
                player_money -= int(bet)
                print("You lost. You now have 💰", player_money)

            if player_money <= 0:
                print("Game Over!")
                return
            if player_money >= 50:
                print("You have over 💰50. You win!")
                return
        else:
            print("Wrong Input! Try Again.")

# Uncomment the function calls below to test each function individually

# guess_random_number(6, 0, 100)
# guess_random_num_linear(5, 0, 10)
# guess_random_num_binary(5, 0, 100)
# guess_menu()
