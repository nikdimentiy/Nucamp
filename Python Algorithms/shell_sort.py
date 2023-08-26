def shell_sort(arr):
    """
    Sorts an array using the shell sort algorithm.

    Args:
        arr: The array to be sorted.

    Returns:
        The sorted array.
    """

    # This is a comment that explains what the function does.

    # This is another comment that explains the purpose of the gap variable.

    gap = len(arr) // 2
    while gap > 0:
        # Iterate over the array, starting from the gap-th element.
        for i in range(gap, len(arr)):
            # This is the current element to be sorted.
            temp = arr[i]

            # This is the index of the element that temp should be swapped with.
            j = i

            # Iterate backwards while the element at j is greater than temp.
            while j >= gap and arr[j - gap] > temp:
                # Move the element at j one position to the right.
                arr[j] = arr[j - gap]

                # Decrement j.
                j -= gap

            # Put temp in its correct position.
            arr[j] = temp

        # Halve the gap.
        gap //= 2

    return arr


arr = [10, 8, 7, 2, 4, 6, 5, 3, 1]

sorted_arr = shell_sort(arr)

print(sorted_arr)
