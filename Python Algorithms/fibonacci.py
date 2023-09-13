def fibonacci(x):
    """
    Calculate the Fibonacci number at position x in the Fibonacci sequence.

    Parameters:
    x (int): The position in the Fibonacci sequence (0-based index).

    Returns:
    int: The Fibonacci number at position x.

    This function uses a recursive approach to calculate Fibonacci numbers.

    Time Complexity:
    The time complexity of this function is O(2^x), which makes it inefficient for large values of x.
    """

    # Base case: if x is 0 or 1, return x
    if x <= 1:
        return x

    # Recursive case: calculate Fibonacci numbers for x-1 and x-2 and sum them
    return fibonacci(x - 1) + fibonacci(x - 2)

# Driver code to test the Fibonacci function
if __name__ == "__main__":
    try:
        n = int(input("Enter a non-negative integer to find its Fibonacci number: "))
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        
        result = fibonacci(n)
        print(f"The Fibonacci number at position {n} is {result}.")
    except ValueError as ve:
        print(f"Error: {ve}")
