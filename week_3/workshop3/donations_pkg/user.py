def login(database, username, password):
    """User registration verification function"""
    for key, value in database.items():
        if key == username and value == password:
            print(f"Welcome back {username}")
            return username
        elif key == username and value != password:
            print(f"Incorrect password for {username}")
            return ""
        else:
            print("User not found. Please register.")
            return ""


def register(database, username):
    """The function of the registration process.
       If the user entered is already registered, an error message is displayed"""
    if username in database:
        print("Username already registered.")
        return ""  # return empty string
    else:
        print(f"Username {username} registered!")
        return username
