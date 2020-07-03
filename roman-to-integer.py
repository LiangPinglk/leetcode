class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        #integer_val = [1, 5, 10, 50, 100, 500, 1000]
    
        # I VX  X LC  C DM
        result = 0
        s_len = len(s)
        limit_index = -1
        for i in range(0, s_len):
            if i <= limit_index:
                continue
            tmp_index = i + 1
            if tmp_index < s_len and roman[s[i]] < roman[s[tmp_index]]:
                if (s[i] == 'I' and s[tmp_index] in ['V', 'X']) or (s[i] == 'X' and s[tmp_index] in ['L', 'C']) or (s[i] == 'C' and s[tmp_index] in ['D', 'M']):
                    #print(s[i], s[tmp_index])
                    #import ipdb
                    #ipdb.set_trace()
                    result += roman[s[tmp_index]] - roman[s[i]]
                    if tmp_index == s_len - 1:
                        return result
                    limit_index = tmp_index
                    continue
            result += roman[s[i]]
        return result

if __name__ == '__main__':
    s = Solution()
    # 1000 900 90 4  1994
    for test in ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']:
        print(test, s.romanToInt(test))


