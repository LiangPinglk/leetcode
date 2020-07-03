class Solution(object):
    def compare(self, i, letter, strs):
        result = True
        for tmp_str in strs:
            try:
                if tmp_str[i] != letter:
                    return False
            except IndexError:
                return False
        return result

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        if len(strs) == 0:
            return result
        first_str = strs[0]
        for i in range(0, len(first_str)):
            if self.compare(i, first_str[i], strs[1:]):
                result += first_str[i]
            else:
                return result
        return result

if __name__ == '__main__':
    s = Solution()
    test = ["flower","flow","flight"]
    print(test, s.longestCommonPrefix(test))
    test = ["dog","racecar","car"]
    print(test, s.longestCommonPrefix(test))
