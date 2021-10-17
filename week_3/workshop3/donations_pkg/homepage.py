def show_homepage():
    """Menu display function"""
    print("         === DonateMe Homepage ===         ")
    print("------------------------------------------")
    print("| 1.    Login       | 2.    Register      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate      | 4.    Show Donation |")
    print("------------------------------------------")
    print("|                 5. Exit                 |")
    print("------------------------------------------")


def donate(username):
    """Donation input function"""
    donation_amt = float(input("Enter amount to donate: "))
    donation = f"{username} donated ${donation_amt}"
    print("Thank you for your donation!")
    return donation  # return string value


def show_donations(donations):
    """Donation output function"""
    print("\n--------- All Donations ---------")
    if not donations:
        print("Currently, there are no donations.")
    else:
        print("\n".join(map(str, donations)))


def total_donations(donations):
    """The function converts a string into a list with a float point numbers in value,
       and calculating the total sum of donations"""
    import re  # import Regular Expression module
    donation_text = (" ".join(map(str, donations)))
    list_of_donation = re.findall(r"[-+]?\d*\.\d+|\d+", donation_text)
    res = [float(i) for i in list_of_donation]
    # calculating the total sum of donations
    total_sum_of_donation = sum(map(float, res))
    print(f"The total donations: *** ${total_sum_of_donation} ***")
