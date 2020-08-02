class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 该题如果使用python字符串自带功能，直接使用字符串的index功能（haystack.index(needle)）就可以得到正确答案，但是这是这不是该算法题考察的初衷，所以不适用该方法
        if not needle:
            return 0
        needle_len = len(needle)
        haystack_len = len(haystack)
        for i in range(0, haystack_len):
            if haystack_len < needle_len + i:
                return -1
            if needle[0] == haystack[i]:
                if haystack[i:i+needle_len] == needle:
                    return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr('a', 'a'))
    print(s.strStr('aedfdf', 'a'))
    print(s.strStr('hello', 'll'))
    print(s.strStr('aaaaa', 'bba'))
    print(s.strStr('hello', 'o'))
