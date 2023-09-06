import math

def jump_search(arr, element):
    """
    Perform a jump search to find the index of an element in a sorted array.

    Args:
        arr (list): A sorted list of elements.
        element: The element to search for.

    Returns:
        int: The index of the element if found, or -1 if not found.
    """

    n = len(arr)
    step = int(math.floor(math.sqrt(n)))  # Calculate the jump step size.
    prev = 0  # Initialize the previous index.

    # Perform the initial jump to the block where the element might be.
    while arr[min(step, n) - 1] < element:
        prev = step
        step += int(math.floor(math.sqrt(n)))

        # If we've reached or exceeded the end of the array, the element is not present.
        if prev >= n:
            return -1

    # Perform linear search within the block for the element.
    while arr[prev] < element:
        prev = prev + 1

        # If we've reached the end of the block without finding the element, it's not present.
        if prev == min(step, n):
            return -1

    # If the element is found at the current index, return the index.
    if arr[prev] == element:
        return prev

    # If the element is not found, return -1.
    return -1

# Driver code to test jump_search
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    element_to_find = 11

    index = jump_search(arr, element_to_find)

    if index != -1:
        print(f"Element {element_to_find} found at index {index}.")
    else:
        print(f"Element {element_to_find} not found in the array.")

