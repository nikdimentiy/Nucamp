class User:
    """Class representing a user."""

    def __init__(self, name, pin, password):
        """Initialize User object with name, pin, and password."""
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, newName):
        """Change the user's name."""
        if len(newName) in range(2, 11):
            self.name = newName
        else:
            print("New username must be between 2 to 10 characters")

    def change_pin(self, newPin):
        """Change the user's PIN."""
        if len(newPin) == 4 and newPin.isnumeric() and newPin != self.pin:
            self.pin = newPin
        else:
            print("New PIN must be 4 numbers only and not the current PIN")

    def change_password(self, newPassword):
        """Change the user's password."""
        if len(newPassword) >= 5 and ' ' not in newPassword and newPassword != self.password:
            self.password = newPassword
            print("Password has been changed")
        else:
            print("New password must be greater than 5 characters, contain no space, and must not be previous")


class BankUser(User):
    """Class representing a bank user."""

    def __init__(self, name, pin, password):
        """Initialize BankUser object with name, pin, and password."""
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def flip_on_hold(self):
        """Toggle the on_hold status of the account."""
        self.on_hold = not self.on_hold

    def show_balance(self):
        """Display the user's account balance."""
        print(self.name, "has an account balance of:", currency_convert(self.balance))

    def withdraw(self, amount):
        """Withdraw money from the user's account."""
        if not self.on_hold:
            if amount > 0 and (amount <= self.balance):
                self.balance -= amount
            else:
                print("Invalid withdraw. Please use amount over $0.00 and lower than your current balance")
        else:
            print("Account is frozen")

    def deposit(self, amount):
        """Deposit money into the user's account."""
        if not self.on_hold:
            if amount > 0:
                self.balance += amount
            else:
                print("Invalid deposit. Please use amount over $0.00")
        else:
            print("Account is frozen")

    def transfer_money(self, receiving_user, amount):
        """Transfer money to another user."""
        if not self.on_hold:
            if amount > 0 and (self.balance >= amount):
                print("\nYou are transferring", currency_convert(amount), "to", receiving_user.name)
                print("Authentication required")
                pin_input = int(input("Enter your PIN: "))
                if pin_input == self.pin:
                    print("Transfer authorized")
                    self.balance -= amount
                    receiving_user.balance += amount
                else:
                    print("Invalid PIN. Transaction canceled.")
            else:
                print("Invalid transfer request. Please transfer amount over $0")
        else:
            print("Account is frozen")

    def request_money(self, requested_from_user, amount):
        """Request money from another user."""
        if not self.on_hold:
            if amount > 0 and (requested_from_user.balance >= amount):
                print("\nYou are requesting $", currency_convert(amount), "from", requested_from_user.name)
                print("User authentication is required...")
                pin_input = int(input("Enter " + str(requested_from_user.name) + "'s pin: "))
                if pin_input == requested_from_user.pin:
                    password_input = input("Enter your password: ")
                    if password_input == self.password:
                        print("Request authorized")
                        requested_from_user.balance -= amount
                        print(requested_from_user.name, "sent", currency_convert(amount))
                        self.balance += amount
                    else:
                        print("Invalid password. Transaction canceled.")
                else:
                    print("Invalid PIN. Transaction canceled.")
            else:
                print("Invalid request. Please use request amount over $0")
        else:
            print("Account is frozen")


def currency_convert(amount):
    """Converts the amount to currency format."""
    return '${:,.2f}'.format(amount)


""" <-----Driver Code for Task 1----->

Dimas = User("Dimas", 1234, "password")
print(Dimas.name, Dimas.pin, Dimas.password)
============================================
"""
