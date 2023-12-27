// Coding interview practice: LeetCode problem -> Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)

package main

import (
	"fmt"
)

// containsDuplicate checks if the given list contains any duplicate elements.
// It returns true if there are duplicates, and false otherwise.
func containsDuplicate(nums []int) bool {
	// Create a map to keep track of unique elements encountered so far.
	numMap := make(map[int]bool)

	// Iterate through each element in the input list.
	for _, num := range nums {
		// Check if the current element is already in the map.
		if numMap[num] {
			// If duplicate found, return true.
			return true
		} else {
			// If not a duplicate, add the element to the map.
			numMap[num] = true
		}
	}

	// If the loop completes without finding duplicates, return false.
	return false
}

func main() {
	// Example usage:
	array1 := []int{1, 2, 3, 4, 5}
	array2 := []int{1, 2, 3, 4, 1}

	// Test cases
	fmt.Println(containsDuplicate(array1)) // Output: false (No duplicates in array1)
	fmt.Println(containsDuplicate(array2)) // Output: true (Duplicates found in array2)
}
