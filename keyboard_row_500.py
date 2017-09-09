class Solution(object):
	def findWords(self, words):
		rows_data = {}
		rows_data['rows_one'] = 'qwertyuiop'
		rows_data['rows_two'] = 'asdfghjkl'
		rows_data['rows_three'] = 'zxcvbnm'
		result = []
		for j in range(len(words)):
			one_data = words[j]
			for k,v in rows_data.items():
				if one_data[0].lower() in rows_data[k]:
					seq=1
					for i in range(1,len(one_data)):
						if one_data[i].lower() in rows_data[k]:
							seq += 1
						else:
							break
					if seq == len(one_data):
						result.append(one_data)
		return result

sol = Solution()
print sol.findWords(["Hello", "Alaska", "Dad", "Peace"])
