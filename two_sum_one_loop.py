class Solution(object):
	def twoSum(self, nums, target):
		nums_dict = {}
		for i in range(len(nums)):
			complement = target - nums[i]
			if nums_dict.has_key(complement):
				if nums_dict[complement]!=i:
					return [nums_dict[complement], i]
			nums_dict[nums[i]] = i

sol = Solution()
print sol.twoSum([2,7,11,15], 9)
