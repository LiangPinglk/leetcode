class Solution(object):
    def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		res = 0
		for num in nums:
			res ^= num
		return res
sol = Solution()
print sol.singleNumber([1,1,2,2,3,3,4,4,5])
