from typing import List


class Solution:
    # 方法一
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     i = 0
    #     nums_len = len(nums)
    #     for j in range(1, nums_len):
    #         if nums[i] != nums[j]:
    #             i += 1
    #             nums[i] = nums[j]
    #     return i+1
    # 方法二
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)
        i = nums_len - 1
        for j in range(nums_len - 2, -1, -1):
            if nums[i] == nums[j]:
                nums.pop(j)
            i -= 1
        # print(nums)
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(s.removeDuplicates([1, 1, 2]))
