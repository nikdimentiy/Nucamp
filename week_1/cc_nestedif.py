def evaluate_price(price):
    """
    This function evaluates the price and provides feedback based on predefined conditions.

    Args:
    price (int): The price to be evaluated.

    Returns:
    None
    """
    # Check if the price is less than 5
    if price < 5:
        print("Price is too low!")  # If true, print "Price is too low!"
    
    # Check if the price is between 5 and 9 (inclusive)
    elif price >= 5 and price <= 9:
        print("Price is almost there!")  # If true, print "Price is almost there!"
    
    # Check if the price is exactly 10
    elif price == 10:
        print("Price is exactly that!")  # If true, print "Price is exactly that!"
    
    # If none of the above conditions are met, assume the price is too high
    else:
        print("Price is too high!")  # Print "Price is too high!"

# Example usage of the function with the given price
priceIsRight = 15
evaluate_price(priceIsRight)
