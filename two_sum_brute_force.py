class Solution(object):
	def twoSum(self, nums, target):
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				if nums[i] == target - nums[j]:
					return [i,j]
sol = Solution()
print sol.twoSum([1,2,3,4,5,6],6)
