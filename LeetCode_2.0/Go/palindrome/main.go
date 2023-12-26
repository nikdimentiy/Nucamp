// Package main provides a solution for the Palindrome Number problem on LeetCode:
// https://leetcode.com/problems/palindrome-number/

package main

import (
	"fmt"
	"strconv"
)

// isPalindrome checks if an integer is a palindrome.
// It converts the integer to a string, reverses the string,
// and compares it with the original string.
// Returns true if the integer is a palindrome, false otherwise.
func isPalindrome(x int) bool {
	// Convert the integer to a string
	strX := strconv.Itoa(x)

	// Convert the string to a slice of runes for reversing
	runesX := []rune(strX)

	// Reverse the slice of runes
	for i, j := 0, len(runesX)-1; i < j; i, j = i+1, j-1 {
		runesX[i], runesX[j] = runesX[j], runesX[i]
	}

	// Convert the reversed slice of runes back to a string
	reversedStrX := string(runesX)

	// Compare the original string with the reversed string
	return strX == reversedStrX
}

func main() {
	// Driver code
	x := 121
	fmt.Println(isPalindrome(x)) // true
	x = -121
	fmt.Println(isPalindrome(x)) // false
	x = 10
	fmt.Println(isPalindrome(x)) // false
	x = -101
	fmt.Println(isPalindrome(x)) // false
	x = 0
	fmt.Println(isPalindrome(x)) // true
}
