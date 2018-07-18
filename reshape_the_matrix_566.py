class Solution(object):
	def matrixReshape(self, nums, r, c):
		if nums[0]
		if r*c == len(nums) + len(nums[0]):
			count = 0
			result = []
			second_level_list = []
			for i in range(len(nums)):
				for j in range(len(nums[0])):
					if count < c:
						second_level_list.append(nums[i][j])
						count += 1
						if count == c:
							result.append(second_level_list)
							second_level_list=[]
							count = 0
			return result
		else:
			return nums

sol = Solution()
print sol.matrixReshape([[1,2],[3,4]],1,4)
print sol.matrixReshape([1,2,3,4],2,2)
