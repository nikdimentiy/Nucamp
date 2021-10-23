import random

print("🌟🌟🌟🌟🌟🌟🌟🌟 WELCOME TO THE GAMEBOX 🌟🌟🌟🌟🌟🌟🌟🌟")
print()
print("<----------Enter your choice of the game:-------------->")
print("********************************************************")
print("Do you want to play with computer or against each other?")
print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
print("Enter: 1 - game with computer")
print("Enter: 2 - game against each other")
print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
print("🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮")
game_one_start = False
game_two_start = False
user_choice = input("Please enter your choice: ").lower()
access_game_attempt = 5

if user_choice == "1":
    game_one_start = True
elif user_choice == "2":
    game_two_start = True
else:
    while access_game_attempt > 0:
        print(
            " ➡➡➡ You input is wrong🚫! Correct your input. Enter --> ❶ || ❷ !!! ↩↩↩ "
        )
        access_game_attempt -= 1
        user_choice = input("Please enter your choice: ").lower()
        if user_choice == "1":
            game_one_start = True
            break
        elif user_choice == "2":
            game_two_start = True
            break

while game_one_start:
    guess = 0
    attempt = 0
    secret = random.randint(1, 100)

    print("I am a very smart🍀 computer and I have a secret  number!🤘")
    print(
        "You have 6 attempts⑥ - to guess it! The guessed number in the range from 1 to 100"
    )
    print(
        "--------------------------------------------------------------------------------"
    )
    game_one_start = input(
        "If you want to play --> Press 'ENTER'✅ <-- If you want to QUIT❌ --> enter 'Q': "
    ).lower()
    if game_one_start == "q":
        break
    while guess != secret and attempt < 6:
        guess = input(" Ⓐ ---> Your attempt <---Ⓐ : ")
        if guess.isnumeric():
            guess = int(guess)
            if guess < secret:
                print("This is less▼ than planned number! "
                      "(you have {} attempts⌛ left):".format(abs(attempt - 5)))
            elif guess > secret:
                print("This is more▲ than planned number! "
                      "(you have {} attempts⌛ left):".format(abs(attempt - 5)))
            attempt += 1
        else:
            print(
                "You entered invalid input!🔥Correct you choice!🔥Only numbersⓃ! Be attention!"
            )
    print("\n")
    if guess == secret:
        print("You are awesome!👌 You guessed it! Congratulations!🌹🌹🌹")
    else:
        print("The attempts are over⛔. You will be lucky next time!🤞")
        print("The secret number is🌏: ", secret)

while game_two_start:
    game_two_start = input(
        "If you want to play --> Press 'ENTER'✅ <-- If you want to QUIT❌ --> enter 'Q': "
    ).lower()
    if game_two_start == "q":
        break

    # Function to print Tic Tac Toe
    def print_tic_tac_toe(values):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
        print('\t_____|_____|_____')

        print("\t     |     |")

        print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
        print("\t     |     |")
        print("\n")

    # Function to print the score-board
    def print_scoreboard(score_board):
        print("\t--------------------------------")
        print("\t✅✅✅✅ SCOREBOARD ✅✅✅✅ ")
        print("\t--------------------------------")

        players = list(score_board.keys())
        print("\t   ", players[0], "\t    ", score_board[players[0]])
        print("\t   ", players[1], "\t    ", score_board[players[1]])

        print("\t--------------------------------\n")

    # Function to check if any player has won
    def check_win(player_pos, cur_player):

        # All possible winning combinations
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],
                [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        # Loop to check if any winning combination is satisfied
        for x in soln:
            if all(y in player_pos[cur_player] for y in x):
                # Return True if any winning combination satisfies
                return True
        # Return False if no combination is satisfied
        return False

    # Function to check if the game is drawn
    def check_draw(player_pos):
        if len(player_pos['X']) + len(player_pos['O']) == 9:
            return True
        return False

    # Function for a single game of Tic Tac Toe
    def single_game(cur_player):
        # Represents the Tic Tac Toe
        values = [' ' for _ in range(9)]

        # Stores the positions occupied by X and O
        player_pos = {'X': [], 'O': []}

        # Game Loop for a single game of Tic Tac Toe
        while True:
            print_tic_tac_toe(values)

            # Try exception block for MOVE input
            try:
                print("Player ", cur_player, " turn. Which box? : ", end="")
                move = int(input())
            except ValueError:
                print("Wrong Input!⛔⛔⛔!! Try Again🐾")
                continue

            # Sanity check for MOVE inout
            if move < 1 or move > 9:
                print("Wrong Input⛔⛔⛔!!! Try Again🐾")
                continue

            # Check if the box is not occupied already
            if values[move - 1] != ' ':
                print("Place already filled. Try again🐾!!")
                continue

            # Updating grid status
            values[move - 1] = cur_player

            # Updating player positions
            player_pos[cur_player].append(move)

            # Function call for checking win
            if check_win(player_pos, cur_player):
                print_tic_tac_toe(values)
                print("Player ", cur_player, " has won the game!!")
                print("\n")
                return cur_player

            # Function call for checking draw game
            if check_draw(player_pos):
                print_tic_tac_toe(values)
                print("Game Drawn")
                print("\n")
                return 'D'

            # Switch player moves
            if cur_player == 'X':
                cur_player = 'O'
            else:
                cur_player = 'X'

    def start_play():
        print(" ✴✴✴✴✴✴✴✴✴✴✴✴✴ TIC TAC TOE ✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
        print("❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇❇")
        print(
            "Tic-Tac-Toe is a 🐝 simple and fun game for 2 players🐝🐝, X and O. \n"
            "💢💢💢 It is played on a 3x3 grid 💢💢💢. \n"
            "⚛⚛⚛ Each player's goal is to make 3 in a row ⚛⚛⚛")
        print("------------------------------------------")
        print("★★★ Player 1 ★★★")
        player1 = input("Enter the name💋 : ")
        print("\n")

        print("★★★ Player 2 ★★★")
        player2 = input("Enter the name💋 : ")
        print("\n")

        # Stores the player who chooses X and O
        cur_player = player1

        # Stores the choice of players
        player_choice = {'X': "", 'O': ""}

        # Stores the options
        options = ['X', 'O']

        # Stores the scoreboard
        score_board = {player1: 0, player2: 0}
        print_scoreboard(score_board)

        # Game Loop for a series of Tic Tac Toe
        # The loop runs until the players quit
        while True:
            # Player choice Menu
            print("*** Turn to choose for *** 🤠", cur_player, "🤠")
            print("Enter ➤ 1 🌠 for X --> press ①")
            print("Enter ➤ 2 🌠 for O --> press ❷")
            print("Enter ➤ 3 🌠 --> to Quit")

            # Try exception for CHOICE input
            try:
                choice = int(input())
            except ValueError:
                print("Wrong Input⛔⛔⛔!!! Try Again🐾\n")
                continue

            # Conditions for player choice
            if choice >= 4 or choice == 0:
                print("Wrong Choice⛔!!!! Try Again🐾\n")
                continue

            if choice == 1:
                player_choice['X'] = cur_player
                if cur_player == player1:
                    player_choice['O'] = player2
                else:
                    player_choice['O'] = player1

            elif choice == 2:
                player_choice['O'] = cur_player
                if cur_player == player1:
                    player_choice['X'] = player2
                else:
                    player_choice['X'] = player1

            elif choice == 3:
                print("Final Scores")
                print_scoreboard(score_board)
                break

            else:
                print("Wrong Choice⛔!!!! Try Again🐾\n")

            # Stores the winner in a single game of Tic Tac Toe
            winner = single_game(options[choice - 1])

            # Edits the scoreboard according to the winner
            if winner != 'D':
                player_won = player_choice[winner]
                score_board[player_won] = score_board[player_won] + 1

            print_scoreboard(score_board)
            # Switch player who chooses X or O
            if cur_player == player1:
                cur_player = player2
            else:
                cur_player = player1

    start_play()
