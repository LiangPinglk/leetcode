from typing import List
def bubble_sort(nums:List[int] )->List[int]:
    for i in range(0, len(nums)):
        for j in range(i, len(nums)-i-1):
            if nums[j] > nums[j +1 ]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
    return nums
 
if __name__ == '__main__':
    print(bubbing_sort([1,7,4,3,2,0]))
    print(bubbing_sort([4,2,45,3,2]))
