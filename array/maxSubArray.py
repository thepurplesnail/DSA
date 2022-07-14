'''
MEDIUM
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

def maxSubArray(nums):
    ans = curr = nums[0]
    for n in nums[1:]:
        # if current total does not drag down n -> add current total to n
        if n + curr > n or curr > n:
            curr += n
        # otherwise current drags n down -> reset current total to n
        else:
            curr = n
        # if current total > ans -> update ans
        ans = max(ans, curr)
    return ans

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))