from typing import List
"""
选择排序：
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
重复第二步，直到所有元素均排序完毕。
"""
def selection_sort(nums:List[int])->List[int]:
    for i in range(0, len(nums)):
        # 最小数的索引
        min_index = i
        for j in range(i + 1, len(nums)):
            # 这里找到最小数的索引
            if nums[j] < nums[i]:
                min_index = j
        if i != j:
            # 如果最小数索引和当前位置的数索引不一样，则交换位置
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
if __name__ == '__main__':
    print(selection_sort([1,7,4,3,2,0]))
    print(selection_sort([4,2,45,3,2]))
    