from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = list()
        for i in range(numRows):
            tmp = list()
            if i == 0:
                tmp = [1]
            else:
                last_list = result[i - 1]
                for j in range(i + 1):
                    if j == 0:
                        tmp.append(last_list[j])
                    elif j == i:
                        tmp.append(last_list[j - 1])
                    else:
                        tmp.append(last_list[j - 1] + last_list[j])
            result.append(tmp)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
