class Solution(object):
	def hammingDistance(self, x, y):
		return bin(x^y).count('1')

sol = Solution()
print sol.hammingDistance(1,4)
