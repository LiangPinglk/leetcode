from typing import List
"""
插入排序：
将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
"""
def insertion_sort(nums:List[int]) -> List[int]:
    for i in range(len(nums)):
        pre_index = i - 1
        current = nums[i]
        while pre_index >= 0 and current < nums[pre_index]:
            nums[pre_index + 1] = nums[pre_index]
            pre_index -= 1
        nums[pre_index + 1] = current
    return nums

if __name__ == '__main__':
    print(insertion_sort([1,7,4,3,2,0]))
    print(insertion_sort([4,2,45,3,2]))