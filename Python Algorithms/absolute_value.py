def custom_abs(x):
    """
    Calculate the absolute value of a number (integer or float).

    Parameters:
        x (int or float): The input number.

    Returns:
        float: The absolute value of the input number.

    Raises:
        TypeError: If the input is not an integer or float.
    """
    if isinstance(x, (int, float)):
        return x if x >= 0 else -x
    else:
        raise TypeError(f"x must be an integer or float, not {type(x)}")

# Example usage
if __name__ == "__main__":
    num = -5.5
    result = custom_abs(num)
    print(f"The absolute value of {num} is {result}")

