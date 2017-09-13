#limit executed
class Solution(object):
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		result = []
		for i in range(1,len(nums)+1):
			if i not in nums:
				result.append(i)
		return result
sol = Solution()
print sol.findDisappearedNumbers([1,2,3,4,1,2,3,4,9])
