# workshop_4


class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, newName):
        if len(newName) in range(2, 11):
            self.name = newName
        else:
            print("New username must be between 2 to 10 characters")

    def change_pin(self, newPin):
        if len(newPin) == 4 and newPin.isnumeric() and newPin != self.pin:
            self.pin = newPin
        else:
            print("New PIN must be 4 numbers only and not the current PIN")

    def change_password(self, newPassword):
        if len(newPassword) >= 5 and ' ' not in newPassword and newPassword != self.password:
            self.password = newPassword
            print("Password has been changed")
        else:
            print(
                "New password must be greater than 5 characters, contain no space, and must not be previous")


def currency_convert(amount):
    return '${:,.2f}'.format(amount)


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def flip_on_hold(self):
        self.on_hold = not self.on_hold

    def show_balance(self):
        print(self.name, "has an account balance of:",
              currency_convert(self.balance))

    def withdraw(self, amount):
        if not self.on_hold:
            if amount > 0 and (amount <= self.balance):
                self.balance -= amount
            else:
                print(
                    "Invalid withdraw. Please use amount over $0.00 and lower than your current balance")
        else:
            print("Account is frozen")

    def deposit(self, amount):
        if not self.on_hold:
            if amount > 0:
                self.balance += amount
            else:
                print("Invalid deposit. Please use amount over $0.00")
        else:
            print("Account is frozen")

    def transfer_money(self, receiving_user, amount):
        if not self.on_hold:
            if amount > 0 and (self.balance >= amount):
                print("\nYou are transferring", currency_convert(
                    amount), "to", receiving_user.name)
                print("Authentication required")
                pin_input = int(input("Enter your PIN: "))
                if pin_input == self.pin:
                    print("Transfer authorized")
                    self.balance -= amount
                    receiving_user.balance += amount

                else:
                    print("Invald PIN. Transaction canceled.")
            else:
                print("Invalid transfer request. Please transfer amount over $0")
        else:
            print("Account is frozen")

    def request_money(self, requested_from_user, amount):
        if not self.on_hold:
            if amount > 0 and (requested_from_user.balance >= amount):
                print("\nYou are requesting $", currency_convert(amount),
                      "from", requested_from_user.name)
                print("User authentication is required...")
                pin_input = int(
                    input("Enter " + str(requested_from_user.name) + "'s pin: "))
                if pin_input == requested_from_user.pin:
                    password_input = input("Enter your password: ")
                    if password_input == self.password:
                        print("Request authorized")
                        requested_from_user.balance -= amount
                        print(requested_from_user.name,
                              "sent", currency_convert(amount))
                        self.balance += amount
                    else:
                        print("Invalid password. Transaction canceled.")
                else:
                    print("Invalid PIN. Transaction canceled.")
            else:
                print("Invalid request. Please use request amount over $0")
        else:
            print("Account is frozen")


""" <-----Driver Code for Task 1----->

Dimas = User("Dimas", 1234, "password")
print(Dimas.name, Dimas.pin, Dimas.password)
============================================
"""

""" <-----Driver Code for Task 2----->
print("\nTask 2")
Dimas = User("Dimas", 1234, "password")
print(Dimas.name, Dimas.pin, Dimas.password)
Dimas.change_name("Dimasik")
Dimas.change_pin(4321)
Dimas.change_password("newpassword")
print(Dimas.name, Dimas.pin, Dimas.password)
============================================
"""

""" <-----Driver Code for Task 3----->
print("\nTask3")
Dimas = BankUser("Dimas", 1234, "password")
print(Dimas.name, Dimas.pin, Dimas.password)
============================================
"""

""" <-----Driver Code for Task 4----->
print("\nTask 4")
Dimas = BankUser("Dimas", 1234, "password")
Dimas.show_balance()
Dimas.deposit(1000)
Dimas.show_balance()
Dimas.withdraw(500)
Dimas.show_balance()
============================================
"""

""" <-----Driver Code for Task 5----->
print("\nTask 5")
Dimas = BankUser("Dimas", 1234, "password")
Julia = BankUser("Julia", 1111, "pass")
Julia.deposit(5000)
Julia.show_balance()
Dimas.show_balance()
Julia.transfer_money(Dimas, 500)
Julia.show_balance()
Dimas.show_balance()
Julia.request_money(Dimas, 250)
Julia.show_balance()
Dimas.show_balance()
==========================================
"""

""" <-- ### Driver Code for Bonus Task ### -->
Dimas = BankUser("Dimas", 1234, "password")
Dimas.deposit(1000)
Dimas.show_balance()
Julia = BankUser("Julia", 4321, "pass")
Dimas.transfer_money(Julia, 100.55)
Julia.show_balance()
Julia.request_money(Dimas, 100.35)
Julia.show_balance()
Dimas.show_balance()
Dimas.withdraw(100)
Dimas.show_balance()
Dimas.flip_on_hold()
Dimas.show_balance()
"""
