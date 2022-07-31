def abs(x):
    if isinstance(x, [int, float]):
        return x if x >= 0 else -x
    else:
        raise TypeError(f"x must be an integer or float not {type(x)}")
# abs() is also an in-built function in Python
