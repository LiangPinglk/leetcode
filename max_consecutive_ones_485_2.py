class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		count = 0
		result = 0
		for i in nums:
			if i==1:
				count += 1
			else:
				result = max(count, result)
				count = 0
		result = max(count, result)
		return result
sol = Solution()
print sol.findMaxConsecutiveOnes([1,1,1,1,0,1,1,1,1,1,1,1,0,1,1])
