class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        x_len = len(x_str)
        for i, v in enumerate(x_str, 1):
            if v != x_str[x_len - i]:
                return False
        return True


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
