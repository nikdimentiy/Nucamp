def fizzbuzz(num):
    """
    A function that prints the FizzBuzz sequence up to a given number.

    Parameters:
    num (int): The number up to which to print the FizzBuzz sequence.

    Returns:
    None
    """

    # Iterate over numbers from 1 to num (exclusive)
    for i in range(1, num):
        # Check if the number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue  # Skip to the next iteration
        # Check if the number is divisible by 3
        if i % 3 == 0:
            print("Fizz")
            continue  # Skip to the next iteration
        # Check if the number is divisible by 5
        if i % 5 == 0:
            print("Buzz")
            continue  # Skip to the next iteration
        # If the number is not divisible by either 3 or 5, print the number itself
        print(i)

# Test the function with a number
fizzbuzz(50)
