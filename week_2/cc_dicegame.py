import random

# Initialize a high score
high_score = 0

def dice_game():
    """
    Simulates a simple dice game where the player can roll two dice and attempt to beat the high score.

    Returns:
        None
    """
    global high_score
    while True:
        print("Current High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        user_choice = (input("Enter your choice: "))
        print("\n")
        if user_choice == "1":
            # Roll two dice
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            print(f"You roll a...{a}")
            print(f"You roll a...{b}")
            print("\n")
            new_score = a + b
            print(f"You have rolled a total of: {new_score} \n")
            # Check if the new score beats the high score
            if new_score > high_score:
                high_score = new_score
                print("New High Score!\n")
        elif user_choice == "2":
            print("Goodbye!\n")
            break
        else:
            print("Unknown Input! Only two choices: 1 <--||--> 2: ")

# Run function
dice_game()
