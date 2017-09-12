#coding:utf-8
class Solution(object):
	def detectCapitalUse(self, word):
		"""
		:type word: str
		:rtype: bool
		"""	
		#自己没想到的方法
		return word.isupper() or word.islower() or word.istitle()
sol = Solution()
print sol.detectCapitalUse('sdfasdfasdf')
