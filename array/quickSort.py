def quicksort(nums):
    helper(nums, 0, len(nums) - 1)
    return nums

def helper(nums, l, r):
    if l >= r:
        return
    lt, gt = partition(nums, l, r)
    print(lt, gt)
    helper(nums, l, lt - 1)
    helper(nums, gt + 1, r)

def partition(nums, lo, hi):
    lt, pivot, gt = lo, nums[lo], hi
    i = lo + 1
    while i <= gt:
        if nums[i] > pivot:
            nums[i], nums[gt] = nums[gt], nums[i]
            gt -= 1
        elif nums[i] < pivot:
            nums[lt], nums[i] = nums[i], nums[lt]
            lt += 1
        else:
            i += 1
    return lt, gt
print(quicksort([5, 2, 8, 2, 11]))