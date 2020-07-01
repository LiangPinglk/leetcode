class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # 判断是否小于0
        lt_zero_flag = True if x < 0 else False
        x = -x if lt_zero_flag else x

        length = 0
        all_number = []

        # 获得各个数字的总长度和各个位上的数字
        while x > 0:
            length += 1
            all_number.append(x%10)
            x = int(x/10)

        # print(all_number, length)

        result = 0
        length -= 1

        # 获得反转数
        for i in all_number:
            if result ==0 and i==0:
                length -= 1
                continue
            result += 0 if i == 0 else i*pow(10, length) 
            length -= 1

        result = -result if lt_zero_flag else result

        # 判断是否在要求的值的范围内
        return result if pow(2,31)-1 >= result >= pow(-2,31) else 0


if __name__ == '__main__':
    import random
    s = Solution()
    test = random.randint(0, pow(10,10))
    test=901000
    print(test)
    print(s.reverse(test))


