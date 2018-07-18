class Solution(object):
    def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		num_dict = {}
		for num in nums:
			num_dict[num]=num_dict.get(num,0)+1
		for k,v in num_dict.items():
			if v==1:
				return k
sol = Solution()
print sol.singleNumber([1,1,2,2,3,3,4,4,5])
