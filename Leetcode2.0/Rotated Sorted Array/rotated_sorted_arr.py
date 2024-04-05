def search(nums, target):
    """
    Search for a target value in a rotated sorted array using binary search.

    Args:
        nums (list): A list of integers representing a rotated sorted array.
        target (int): The value to search for in the array.

    Returns:
        int: The index of the target value if found, otherwise -1.

    """

    def find_pivot(nums):
        """
        Find the index of the pivot element in the rotated sorted array.

        Args:
            nums (list): A list of integers representing the rotated sorted array.

        Returns:
            int: The index of the pivot element.
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if mid < high and nums[mid] > nums[mid + 1]:  # Pivot found
                return mid + 1
            if mid > low and nums[mid - 1] > nums[mid]:
                return mid
            # Shrink the search space based on the sorted part
            if nums[low] <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return 0  # Array was not rotated

    pivot = find_pivot(nums)
    low, high = 0, len(nums) - 1

    # Determine which half the target might be in
    if nums[pivot] <= target <= nums[high]:
        low = pivot
    else:
        high = pivot - 1

    # Standard binary search in the chosen half
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found


# Example usage
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = search(nums, target)
print(result)  # Output: 4
