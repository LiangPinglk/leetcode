package main

import "fmt"

func searchInsert(nums []int, target int) int {
	for i, num := range nums {
		if target <= num {
			return i
		}
	}
	return len(nums)
}
func main() {
	var test = []int{1, 3, 5, 6}
	fmt.Printf("%d\n", searchInsert(test, 5))
	fmt.Printf("%d\n", searchInsert(test, 2))
	fmt.Printf("%d\n", searchInsert(test, 7))
	fmt.Printf("%d\n", searchInsert(test, 6))
	fmt.Printf("%d\n", searchInsert(test, 0))
	fmt.Printf("%d\n", searchInsert(test, 5))
}
