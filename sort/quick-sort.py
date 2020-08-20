"""
快速排序：
https://wiki.jikexueyuan.com/project/easy-learn-algorithm/fast-sort.html
https://zhuanlan.zhihu.com/p/63227573
"""


def quick_sort(nums, i, j):
    if i >= j:
        return
    pivot = nums[i]
    low = i
    high = j
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= pivot:
            i += 1
        nums[j] = nums[i]
    nums[j] = pivot
    quick_sort(nums, low, i - 1)
    quick_sort(nums, i + 1, high)
    return nums


if __name__ == "__main__":
    nums = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    print(quick_sort(nums, 0, len(nums) - 1))
