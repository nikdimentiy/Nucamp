def quick_sort(arr):
    """
    Sorts an array in ascending order using the quick sort algorithm.

    Args:
        arr: The array to be sorted.

    Returns:
        The sorted array.
    """

    # Check if the array is empty or has only one element.

    if len(arr) < 2:
        return arr

    # Choose the pivot element.

    pivot = arr.pop()

    # Create two empty lists to store the elements smaller and greater than the pivot.

    greater = []
    lesser = []

    # Iterate over the array and add elements to the appropriate list.

    for element in arr:
        if element > pivot:
            greater.append(element)
        else:
            lesser.append(element)

    # Recursively sort the two sub-arrays.

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


# Driver code

arr = [10, 8, 2, 7, 3, 5, 9, 6, 1]

print("Unsorted array:", arr)

sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)

