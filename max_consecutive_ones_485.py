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
				result = max(count, result)
			else:
				count = 0
		return result
sol = Solution()
print sol.findMaxConsecutiveOnes([1,1,1,1,0,1,1,1,1,1,1,1,0,1,1])
