class Solution(object):
	def nextGreaterElement(self, findNums, nums):
		loop_count = 0
		result_dic = {}
		for i in range(len(findNums)):
			flag = False
			if loop_count < len(nums):
				for j in range(loop_count,len(nums)):
					if findNums[i] < nums[j]:
						flag = True
						loop_count = j
						result_dic[i] = j
					else:
						result_dic[i] = -1
			else:
				result_dic[i] = -1
		result = []
		return result_dic.values()
					
sol = Solution()
print sol.nextGreaterElement([4,1,2],[1,3,4,2])
print sol.nextGreaterElement([2,4],[1,2,3,4])
print sol.nextGreaterElement([4,1,2],[1,2,3,4])
