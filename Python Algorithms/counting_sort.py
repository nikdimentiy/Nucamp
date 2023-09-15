def counting_sort(arr):
    """Sorts an array using the counting sort algorithm.

    Args:
        arr: A list of integers to be sorted.

    Returns:
        A list of integers sorted in ascending order.
    """

    # Find the maximum element in the array.
    maxEl = max(arr)

    # Create a count array to store the number of occurrences of each element in the array.
    countArrayLength = maxEl + 1
    countArray = [0] * countArrayLength

    # Count the number of occurrences of each element in the array.
    for el in arr:
        countArray[el] += 1

    # Calculate the cumulative sum of the count array.
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i - 1]

    # Create an output array to store the sorted elements.
    outputArray = [0] * len(arr)

    # Iterate over the array in reverse order and place each element in its correct position in the output array.
    i = len(arr) - 1
    while i >= 0:
        currentEl = arr[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray


# Create an unsorted array.
arr = [5, 3, 2, 1, 4]

# Sort the array using the counting sort algorithm.
sortedArray = counting_sort(arr)

# Print the sorted array.
print(sortedArray)

