import random

diamonds = [
    "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD",
    "KD"
]
hand = []

# Loop until there are cards remaining
while diamonds:
    user_choice = input("Press 'ENTER' or type 'Q' to quit: ")
    # Check if the user wants to quit
    if user_choice.lower() == "q":
        break
    else:
        # Choose a random card from the remaining cards
        random_card_choice = random.choice(diamonds)
        # Print the card chosen for the current hand
        print("Your hand: ", str([random_card_choice]))
        # Add the card to the hand
        hand.append(random_card_choice)
        # Remove the card from the remaining cards
        diamonds.remove(random_card_choice)
        # Print the current hand and remaining cards
        print(f"Your hand: {hand}")
        print(f"Remaining cards: {diamonds}")

# If there are no more cards remaining, print a message
if not diamonds:
    print("There are no more cards to pick.")
