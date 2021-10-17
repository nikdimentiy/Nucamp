from donations_pkg.homepage import show_homepage, donate, show_donations, total_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}  # define the initial state of the database
donations = []  # define the initial state of the list of donations
# define the initial state of the variable (authorized user)
autorized_user = ""

show_homepage()  # Menu display function

if not autorized_user:
    print("You must be logged in to donate.")
else:
    print(f"Logged in as: {autorized_user}")

while True:
    choice = input("Choose an option: ")
    choice = choice.lower()
    print()
    if choice == "1" or choice == "login":  # processing o various options for entering the menu
        username = input("Enter username: ")
        username = username.lower()  # case sensitive input -> problem-solving
        password = input("Enter password: ")
        password = password.lower()  # case sensitive input -> problem-solving
        print()
        autorized_user = login(database, username, password)
        print()
        show_homepage()
        if not autorized_user:
            pass
        else:
            print(f"Logged in as: {autorized_user}")

    elif choice == "2" or choice == "register":  # processing o various options for entering the menu
        username = input("Enter username: ")
        username = username.lower()  # case sensitive input -> problem-solving
        password = input("Enter password: ")
        password = password.lower()  # case sensitive input -> problem-solving
        print()
        autorized_user = register(database, username)
        print()
        if len(autorized_user) == 0:
            pass
        else:
            database[username] = password
        show_homepage()
        print(f"Logged in as: {autorized_user}")

    elif choice == "3" or choice == "donate":  # processing o various options for entering the menu
        if not autorized_user:
            print("You are not logged in.")
        else:
            donation = donate(autorized_user)
            donations.append(donation)
        show_homepage()
        print(f"Logged in as: {autorized_user}")

    elif choice == "4" or choice == "show donations":
        show_donations(donations)
        # the function of display the total sum of donation
        total_donations(donations)
        show_homepage()
        print(f"Logged in as: {autorized_user}")

    elif choice == "5" or choice == "exit":  # processing o various options for entering the menu
        print("Goodbye! -> Have a nice day!")
        print("*** Leaving DonateMe ***")
        break
    else:
        print("You entered the wrong input. Try one more time!")
