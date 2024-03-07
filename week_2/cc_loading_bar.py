"""
This program simulates a loading progress indicator.
"""

def loading_progress():
    """
    Prints loading progress and milestones.
    """
    # Iterate through loading amounts from 0 to 100 in steps of 5
    for amount_loaded in range(0, 101, 5):
        print(amount_loaded)

        # Check for loading milestones and print corresponding messages
        if amount_loaded == 25:
            print("1/4 of the way there")
        elif amount_loaded == 50:
            print("1/2 of the way there")
        elif amount_loaded == 75:
            print("3/4 of the way there")
        elif amount_loaded == 100:
            print("Loading complete!")

# Call the function to simulate loading progress
loading_progress()
