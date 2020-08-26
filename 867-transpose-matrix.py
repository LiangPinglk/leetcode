from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)
        column = len(A[0])
        result = []
        for i in range(column):
            tmp = []
            for j in range(row):
                tmp.append(A[j][i])
            result.append(tmp)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(s.transpose([[1, 2, 3], [4, 5, 6]]))
