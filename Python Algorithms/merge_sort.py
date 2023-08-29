def merge_sort(arr):
    """
    Sorts a list using the merge sort algorithm.
    
    Args:
    arr (list): The list to be sorted.
    
    Returns:
    list: A new sorted list.
    """
    def merge(left, right):
        """
        Merge two sorted lists into a single sorted list.
        
        Args:
        left (list): The left sorted list.
        right (list): The right sorted list.
        
        Returns:
        list: The merged sorted list.
        """
        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

# Driver code
if __name__ == "__main__":
    input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    sorted_list = merge_sort(input_list)
    print("Sorted list:", sorted_list)
