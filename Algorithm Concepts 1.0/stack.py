# Initialize the stacks
stack = []      # Main stack to hold the items
min_stack = []  # Stack to keep track of the minimum values
max_stack = []  # Stack to keep track of the maximum values

def push(item):
    """
    Push an item onto the main stack and update the min and max stacks accordingly.

    Parameters:
    item (int): The item to be pushed onto the stack.
    """
    stack.append(item)  # Add the item to the main stack
    
    # Update min_stack if the new item is less than or equal to the current minimum
    if not min_stack or item <= min_stack[-1]:
        min_stack.append(item)
    
    # Update max_stack if the new item is greater than or equal to the current maximum
    if not max_stack or item >= max_stack[-1]:
        max_stack.append(item)

def pop():
    """
    Remove and return the top item from the main stack, updating the min and max stacks.

    Returns:
    int: The item removed from the top of the stack.

    Raises:
    IndexError: If the stack is empty.
    """
    if not stack:
        raise IndexError("pop from empty stack")  # Raise an error if the stack is empty
    item = stack.pop()  # Remove the top item from the main stack
    
    # Update min_stack if the popped item is the current minimum
    if item == min_stack[-1]:
        min_stack.pop()
    
    # Update max_stack if the popped item is the current maximum
    if item == max_stack[-1]:
        max_stack.pop()
    
    return item  # Return the popped item

def peek():
    """
    Return the top item of the main stack without removing it.

    Returns:
    int: The item at the top of the stack.

    Raises:
    IndexError: If the stack is empty.
    """
    if not stack:
        raise IndexError("peek from empty stack")  # Raise an error if the stack is empty
    return stack[-1]  # Return the top item

def size():
    """
    Return the number of items in the main stack.

    Returns:
    int: The size of the stack.
    """
    return len(stack)  # Return the size of the main stack

def get_min():
    """
    Return the minimum item from the stack without removing it.

    Returns:
    int: The minimum item in the stack.

    Raises:
    IndexError: If the min_stack is empty.
    """
    if not min_stack:
        raise IndexError("min from empty stack")  # Raise an error if min_stack is empty
    return min_stack[-1]  # Return the current minimum

def get_max():
    """
    Return the maximum item from the stack without removing it.

    Returns:
    int: The maximum item in the stack.

    Raises:
    IndexError: If the max_stack is empty.
    """
    if not max_stack:
        raise IndexError("max from empty stack")  # Raise an error if max_stack is empty
    return max_stack[-1]  # Return the current maximum

# Example usage
if __name__ == "__main__":
    push(3)
    push(5)
    print("Current Min:", get_min())  # Output: 3
    print("Current Max:", get_max())  # Output: 5
    push(2)
    push(1)
    print("Current Min:", get_min())  # Output: 1
    print("Current Max:", get_max())  # Output: 5
    pop()
    print("Current Min:", get_min())  # Output: 2
    print("Current Max:", get_max())  # Output: 5
    pop()
    print("Current Min:", get_min())  # Output: 3
    print("Current Max:", get_max())  # Output: 5
