class Solution(object):
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		result = list(set(range(1,len(nums)+1))-set(nums))
		result.sort()
		return result
sol = Solution()
print sol.findDisappearedNumbers([1,2,3,4,1,2,3,4,9])
