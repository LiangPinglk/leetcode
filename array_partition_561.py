class Solution(object):
	def arrayPairSum(self, nums):
		result = 0
		nums.sort()
		for i in range(len(nums)):
			if i%2!=0:
				result += min(nums[i-1],nums[i])
		return result

sol = Solution()
import ipdb
ipdb.set_trace()
print sol.arrayPairSum([1,1])
