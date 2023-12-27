# Coding interview practice: LeetCode problem -> Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)


def containsDuplicate(nums):
    """
    Check if the given list contains any duplicate elements.

    Args:
    - nums (List[int]): The input list of integers.

    Returns:
    - bool: True if there are duplicates, False otherwise.
    """
    # Create an empty set to keep track of unique elements encountered so far.
    num_set = set()

    # Iterate through each element in the input list.
    for num in nums:
        # Check if the current element is already in the set.
        if num in num_set:
            # If duplicate found, return True.
            return True
        else:
            # If not a duplicate, add the element to the set.
            num_set.add(num)

    # If the loop completes without finding duplicates, return False.
    return False


# Example usage:
array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 3, 4, 1]

# Test cases
print(containsDuplicate(array1))  # Output: False (No duplicates in array1)
print(containsDuplicate(array2))  # Output: True (Duplicates found in array2)
