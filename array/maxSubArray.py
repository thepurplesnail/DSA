'''
MEDIUM
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''


def isUnique(smaller, bigger):
    smaller = set(smaller)
    for bArr in bigger:
        if smaller == set(bArr):
            return False
    return True

def maxSubArray(nums):
    ans = []
    # for each element in nums:
    for i in range(len(nums)):
        stored = set()
        # target is inverse of element
        target = -1 * nums[i]
        # find two other elements that add up to target
        for n in nums[i + 1:]:
            diff = target - n
            # only append them to answer if it is unique
            if diff in stored and isUnique([diff, n, nums[i]], ans):
                ans.append([diff, n, nums[i]])
            else:
                stored.add(n)
    return ans

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))