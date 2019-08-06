class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        for i in range(nums_len):
            diff = target - nums[i]
            j = i + 1
            for j in range(j, nums_len):
                if nums[j] == diff:
                    return [i, j]


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([3, 2, 4], 6))
