package main

import "fmt"

func search(nums []int, target int) int {
	pivot := findPivot(nums)

	low, high := 0, len(nums)-1

	// Determine which half the target might be in
	if nums[pivot] <= target && target <= nums[high] {
		low = pivot
	} else {
		high = pivot - 1
	}

	// Standard binary search in the chosen half
	for low <= high {
		mid := (low + high) / 2 // Corrected integer division
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return -1 // Target not found
}

func findPivot(nums []int) int {
	low, high := 0, len(nums)-1

	for low <= high {
		mid := (low + high) / 2                    // Corrected integer division
		if mid < high && nums[mid] > nums[mid+1] { // Pivot found
			return mid + 1
		}
		if mid > low && nums[mid-1] > nums[mid] {
			return mid
		}

		// Shrink the search space based on the sorted part
		if nums[low] <= nums[mid] {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return 0 // Array was not rotated
}

func main() {
	nums := []int{4, 5, 6, 7, 0, 1, 2}
	target := 0
	result := search(nums, target)
	fmt.Println(result) // Output: 4
}
