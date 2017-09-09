class Solution(object):
	def judgeCircle(self,moves):
		represent_ud = {'U':-1,'D':1}
		represent_lr = {'L':-1,'R':1}
		flag_ud = 0
		flag_lr = 0
		for i in range(len(moves)):
			if represent_ud.has_key(moves[i]):
				flag_ud += represent_ud[moves[i]]
			if represent_lr.has_key(moves[i]):
				flag_lr += represent_lr[moves[i]]
		if flag_lr == 0 and flag_ud == 0:
			return True
		else:
			return False

sol = Solution()
print sol.judgeCircle('UD')
print sol.judgeCircle('LL')

