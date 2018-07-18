class Solution(object):
	def reverseWords(self, s):
		result = ''
		for i in s.split(' '):
			result += i[::-1]+' '
		return result.strip()
			
sol = Solution()
print sol.reverseWords("Let's take LeetCode contest")
