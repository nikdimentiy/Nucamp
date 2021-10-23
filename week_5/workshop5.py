import random


def guess_random_number(tries, start, stop):
    number = random.randint(start, stop)
    past_guess = []
    while tries != 0:
        print("🔥 Number of tries left: 🔥", tries)
        while True:
            guess = input(f"Guess a number between {start} and {stop}: ")

            if guess.isnumeric() == False or (int(guess) < start or int(guess) > stop):
                print(
                    f"Please enter ONLY numbers between --> {start} and {stop} <--")
            elif guess in past_guess:
                print(
                    f"You already guessed😎 number {guess} <-- Please try again -->")
            else:
                past_guess.append(guess)
                # print(past_guess)
                break
        if int(guess) == number:
            print("🌹🌹🌹 YES! It's the correct answer! 🌹🌹🌹")
            return
        if int(guess) < number:
            print("Guess higher!🔺")
        else:
            print("🔻Guess lower!")
        tries -= 1
        if tries == 0:
            print("You've used all your tries.❌❌❌ You failed. ❌❌❌")
            print(f"The guess number is {number}🌼!")
            return


def guess_random_num_linear(tries, start, stop):
    number = random.randint(start, stop)
    print("The number for the program to guess is🍀:", number)

    for i in range(start, stop + 1):
        print("Number of tries left:📡", tries)
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
    number = random.randint(start, stop)
    print("Random number to find:🍀", number)

    while start <= stop:
        pivot = (start + stop) // 2
        if pivot == number:
            print("🟩🟩🟩 Found it! 🟩🟩🟩", number)
            return
        if pivot > number:
            stop = pivot - 1
            print("🔻Guessing lower!")
        else:
            start = pivot + 1
            print("Guessing higher!🔺")
        tries -= 1
        if tries == 0:
            print("❌❌❌ Your program failed to find the number. ❌❌❌")
            return


def guess_menu():
    tries = int(input("\n🔰 Enter number of tries 🔰: "))
    start = int(input("Enter start value❎: "))
    stop = int(input("Enter end value⛔: "))

    while True:
        method = input(
            "\nPress 1 to guess manually: \n"
            "Press 2 to search linearly: \n"
            "Press 3 to perform binary search: \n"
            "Press 'Q' to quit: ").lower()
        if method.isnumeric():
            if method == '1':
                guess_random_number(tries, start, stop)
                continue
            if method == '2':
                guess_random_num_linear(tries, start, stop)
                continue
            if method == '3':
                guess_random_num_binary(tries, start, stop)
                continue
        elif method == 'q':
            break
        else:
            print()
            print(
                "Wrong Input ⛔⛔⛔!!! Try Again🐾! ONLY NUMBERS! --> 1 - 2 - 3 or 'Quit' : \n")
            continue


def gambling_mode():
    player_money = 10
    while True:
        print("\n")
        print("Your balance is: 💲", player_money)
        print("✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
        print("❗Make a bet. Will computer guess correctly or not❗")
        call = input(
            "Enter 'Y' --> to guess computer WILL✅ guess the correct number🎰\n"
            "Enter 'N' --> to guess computer WILL NOT🛑 guess the correct number\n"
            "------------------------------------------------------------------\n"
            "Enter your prediction: ▶ 'Y' [yes] 🕵 or [no] ▶  'N': ").lower()
        print("\n")
        bet = input("How many dollars will you bet? Enter 1 to 10: ")

        if bet.isnumeric():
            result = guess_random_num_linear(5, 0, 10)
            if result == True and call == 'y':
                player_money += int(bet)
                print("💸💸💸💸 You won! You now have 💰💰💰💲", player_money)
            elif result == False and call == 'y':
                player_money -= int(bet)
                print("---> You lost. You now have 💰💰💰💲", player_money)
            elif result == True and call == 'n':
                player_money -= int(bet)
                print("---> You lost. You now have 💰💰💰💲", player_money)
            elif result == False and call == 'n':
                player_money += int(bet)
                print("💸💸💸💸 You won! You now have 💰💰💰💲", player_money)

            if player_money <= 0:
                print("😭😭😭 Game Over 💢💢💢")
                return
            if player_money >= 50:
                print("🤑🤑🤑 You have over 💰💰💰💲50. You win! 🎇🎇🎇")
                return
        else:
            print()
            print("Wrong Input ⛔⛔⛔!!! Try Again🐾\n")
            continue


# Test Driver Code 1ssss
# guess_random_number(6, 0, 100)

# Test Task 2
# guess_random_num_linear(5, 0, 10)

# Test Task 3
# guess_random_num_binary(5, 0, 100)

# Bonus Task 2
# guess_menu()

# Bonus Task 4
# gambling_mode()
