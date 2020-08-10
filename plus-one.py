from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      """
      利用循环，模拟两数的加法运算，num + 1
      """
      digits_len = len(digits)
      for i in range(digits_len-1, -1, -1):
        tmp_sum = digits[i] + 1
        if tmp_sum < 10:
            digits[i] = tmp_sum 
            return digits
        else: 
          digits[i] = tmp_sum%10
          if i == 0:
            return [1] + digits


if __name__ == '__main__':
  s = Solution()
  print(s.plusOne([4,3,2,1]))
  print(s.plusOne([9,9,9,9]))
  print(s.plusOne([9]))
  print(s.plusOne([8,9,9,9]))