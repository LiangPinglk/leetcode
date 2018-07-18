class Solution(object):
	def detectCapitalUse(self, word):
		"""
		:type word: str
		:rtype: bool
		"""
		if word[0].isupper():
			if len(word) > 1:
				if word[1].isupper():
					for i in range(1,len(word)):
						if word[i].islower():
							return False
					return True
				else:
					for i in range(1,len(word)):
						if word[i].isupper():
							return False
					return True
			else:
				return True
		else:
			if len(word) > 1:
				for i in range(1,len(word)):
					if word[i].isupper():
						return False
				return True
			else:
				return True
					
sol = Solution()
print sol.detectCapitalUse('sdfasdfasdf')
