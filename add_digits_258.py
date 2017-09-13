class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = 0
        while(num > 9):
            tmp += num%10
            num = num/10
            num += tmp
            tmp = 0
        return num
