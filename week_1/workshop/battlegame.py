"""
    ---> THE FIRST PROGRAM-GAME IN NUCAMP BOOTCAMP <---
"""

# announce (declare) game characters for the game

wizard = "Wizard"
elf = "Elf"
human = "Human"
ork = "Ork"

# set hitpoints for each game characters (which means remaining health)

wizard_hp = 70
elf_hp = 100
human_hp = 150
ork_hp = 200

# set damage indicator for each game characters (how hard they hit)
wizard_damage = 150
elf_damage = 100
human_damage = 20
ork_damage = 40

# declare the main opponent in the game -> Dragon, and set health point and damage indicator
dragon_hp = 300
dragon_damage = 50

# prompt the player to choose from a list options
# and assign the selection result to the appropriate variables
flag = True
while flag:
    while True:
        print("1)   Wizard")
        print("2)   Elf")
        print("3)   Human")
        print("4)   Ork")
        character = input("Choose your character:  <--||-->  To quit from the game press the 'Q' button: ")
        character = character.lower()
        if character == 'q':
            flag = False
            break
        if character == "1" or character == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character == "2" or character == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character == "3" or character == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif character == "4" or character == "ork":
            character = ork
            my_hp = ork_hp
            my_damage = ork_damage
            break
        else:
            print("Unknown character")
    if character == 'q':
        break
    else:
        print("You have chosen the character:", character)
        print("Health: ", my_hp)
        print("Damage: ", my_damage)

    # battle with Dragon
    while flag:
        dragon_hp -= my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now:", dragon_hp)
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            print("____________________________________")
            break
        my_hp -= dragon_damage
        print("The Dragon strikes back at", character)
        print("The", str(character) + "'s" + " hitpoints are now:", my_hp)
        if my_hp <= 0:
            print("The", character, "has lost the battle")
            print("____________________________________")
            break

print()
print("Game over!")

