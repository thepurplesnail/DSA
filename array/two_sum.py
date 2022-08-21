'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

E.g.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

def twoSum(nums, target):
    stored = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in stored:
            return [i, stored[diff]]
        else:
            stored[nums[i]] = i

print(twoSum([2,7,11,15], 9))

def quicksort(nums):
    helper(nums, 0, len(nums) - 1)
    return nums

def helper(nums, l, r):
    if l >= r:
        return
    lt, gt = partition(nums, l, r)
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
print(quicksort([2,8,2,1,5]))