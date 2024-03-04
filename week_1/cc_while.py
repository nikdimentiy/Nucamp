def iterate_and_print():
    """
    This function demonstrates the use of a while loop with conditions and continues
    to iterate through numbers from 1 to 10 and prints them based on certain conditions.
    """
    x = 0  # Initialize x with 0
    
    # Continue looping until x becomes 10
    while x != 10:
        x = x + 1  # Increment x by 1 in each iteration
        
        # Check if x is less than 5
        if x < 5:
            print(x)  # If true, print the value of x
        
        # Check if x is exactly 6
        elif x == 6:
            print(x)  # If true, print the value of x
            continue  # Skip the rest of the loop and start the next iteration
        
        # Check if x is between 5 and 8 (inclusive), but not 6
        elif x >= 5 and x <= 8:
            print(
                "x is bigger than or equal to 5, and less than or equal to 8, but not 6. It is:",
                x)  # If true, print the message along with the value of x
        
        # If none of the above conditions are met, x must be greater than 8
        else:
            print("x is bigger than 8. It is:", x)  # Print the message along with the value of x

# Call the function to execute the code
iterate_and_print()

