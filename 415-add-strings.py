class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        num1_len = len(num1) - 1
        num2_len = len(num2) - 1
        index_diff = num1_len - num2_len
        other_add = 0
        for i in range(num1_len, -1, -1):
            j = i - index_diff
            if j < 0:
                if other_add == 1:
                    tmp = int(num1[i]) + other_add
                    result.append(str(tmp % 10))
                    other_add = 1 if tmp >= 10 else 0
                else:
                    result.append(num1[i])
            else:
                tmp = int(num1[i]) + int(num2[j]) + other_add
                result.append(str(tmp % 10))
                other_add = 1 if tmp >= 10 else 0
        for i in range(- index_diff - 1, -1, -1):
            if other_add == 1:
                tmp = int(num2[i]) + other_add
                result.append(str(tmp % 10))
                other_add = 1 if tmp >= 10 else 0
            else:
                result.append(num2[i])
        if other_add == 1:
            result.append(str(other_add))
        final_result = ''
        for i in range(len(result) - 1, -1, -1):
            final_result += result[i]
        return final_result


if __name__ == '__main__':
    s = Solution()
    print(s.addStrings('123456', '1234567890'))
    print(s.addStrings('1234567890', '123456'))
    print(s.addStrings('1', '9'))
