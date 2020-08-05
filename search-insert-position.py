from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        nums_len = len(nums)
        for i in range(0, nums_len):
            if nums[i]>=target:
                return i
        return nums_len
if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6], 5))
    print(s.searchInsert([1,3,5,6], 2))
    print(s.searchInsert([1,3,5,6], 7))
    print(s.searchInsert([1,3,5,6], 6))
    print(s.searchInsert([1,3,5,6], 0))
    print(s.searchInsert([1,3,5,6], 5))