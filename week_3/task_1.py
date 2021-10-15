import random

diamonds = [
    "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD",
    "KD"
]
hand = []

while diamonds:
    user_choice = input("Press 'ENTER' or type 'Q'--> for quit: ")
    if user_choice.lower() == "q":
        break
    else:
        random_card_choice = random.choice(diamonds)
        print("Your hand: ", str([random_card_choice]))
        hand.append(random_card_choice)
        diamonds.remove(random_card_choice)
        print(f"Your hand:  {hand}")
        print(f"Remaining cards: {diamonds}")
if not diamonds:
    print("There are no more cards to pick.")
