def siftdown(arr, start, end):
    """
    Perform a sift-down operation in a max-heap to maintain the heap property.

    Args:
    arr (list): The input list representing the heap.
    start (int): The index to start the sift-down operation from.
    end (int): The index indicating the end of the heap.

    Returns:
    None
    """
    root = start
    while True:
        child = root * 2 + 1  # Left child index
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1  # Choose the larger child
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child  # Move down the tree
        else:
            break  # Heap property is maintained

def heapsort(arr):
    """
    Sort a list using the heapsort algorithm.

    Args:
    arr (list): The input list to be sorted.

    Returns:
    list: The sorted list.
    """
    # Heapify the input list
    for start in range((len(arr) - 2) // 2, -1, -1):
        siftdown(arr, start, len(arr) - 1)

    # Extract elements from the max-heap one by one
    for end in range(len(arr) - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        siftdown(arr, 0, end - 1)

    return arr

# Driver code for testing
if __name__ == "__main__":
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = heapsort(unsorted_list)
    print("Unsorted List:", unsorted_list)
    print("Sorted List:", sorted_list)
