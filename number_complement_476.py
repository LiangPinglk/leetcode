class Solution(object):
	def findComplement(self, num):
		bin_str = bin(num)
		bin_str_complement = '0b'
		bin_list = []
		for i in range(len(bin_str)):
			if bin_str[i] == '1':
				for k in range(i,len(bin_str)):
					if bin_str[k]=='0':
						bin_list.append('1')
					elif bin_str[k] =='1':
						bin_list.append('0')
				break
		bin_str_complement +=''.join(bin_list)
		return int(bin_str_complement,2)

sol = Solution()
print sol.findComplement(1)
