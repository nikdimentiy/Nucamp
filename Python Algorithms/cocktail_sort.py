def cocktailSort(A):
    """
    Sort a list using the Cocktail Sort algorithm.

    Args:
        A (list): The list to be sorted.

    Returns:
        None: The list is sorted in-place.
    """
    up = range(len(A) - 1)

    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]  # Swap elements if out of order
                    swapped = True
            if not swapped:
                return  # If no swaps were made in this pass, the list is sorted

# Driver code
if __name__ == "__main__":
    my_list = [4, 2, 9, 6, 1, 5]
    print("Original List:", my_list)
    
    cocktailSort(my_list)
    
    print("Sorted List:", my_list)

