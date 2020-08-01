from typing import List


class Solution:
    # 方法1
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3, 2, 2, 3], 3))
    print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
