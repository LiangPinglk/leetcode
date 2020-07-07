class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return True if len(s) == 0 else False

if __name__ == '__main__':
    s = Solution()
    test = "()"
    print(test, s.isValid(test))
    test = '()[]{}'
    print(test, s.isValid(test))
    test = "(]"
    print(test, s.isValid(test))
    test = "([)]"
    print(test, s.isValid(test))
    test = "{[]}"
    print(test, s.isValid(test))
    test = "){"
    print(test, s.isValid(test))
    test = "()[]{}"
    print(test, s.isValid(test))
    test =  "(()("
    print(test, s.isValid(test))