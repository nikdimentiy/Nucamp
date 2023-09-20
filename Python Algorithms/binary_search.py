def binary_search(l, value, LOW=0, TOP=-1):
    """
    Perform binary search to find the index of 'value' in the sorted list 'l'.

    Args:
    l (list): A sorted list of elements.
    value: The element to search for.
    LOW (int, optional): The lower bound of the search range. Defaults to 0.
    TOP (int, optional): The upper bound of the search range. Defaults to -1, which means the entire list.

    Returns:
    int: The index of 'value' in the list 'l' if found, or -1 if not found.
    """

    if not l:
        return -1

    if TOP == -1:
        TOP = len(l) - 1

    if LOW >= TOP:
        if l[LOW] == value:
            return LOW
        else:
            return -1

    MID = (LOW + TOP) // 2

    if l[MID] > value:
        return binary_search(l, value, LOW, MID - 1)
    elif l[MID] < value:
        return binary_search(l, value, MID + 1, TOP)
    else:
        return MID

# Driver code to test the binary_search function
if __name__ == "__main__":
    sorted_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    search_value = 12
    result = binary_search(sorted_list, search_value)
    if result != -1:
        print(f"{search_value} found at index {result}")
    else:
        print(f"{search_value} not found in the list.")
