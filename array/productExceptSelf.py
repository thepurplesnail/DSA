'''
MEDIUM
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

E.g.
Input: nums = [1,2,3,4]
            pref = [1,1,2,6]
            ans = [24,12,8,6]
Output: [24,12,8,6]
'''

def productExceptSelf(nums):
    ans = [1] * len(nums)
    tot = 1
    # populate ans with prefix product
    for i in range(len(nums)):
        ans[i] = tot
        tot *= nums[i]
    tot = 1
    # multiply elements in ans by suffix product
    for i in reversed(range(len(nums))):
        ans[i] *= tot
        tot *= nums[i]
    return ans

print(productExceptSelf([1,2,3,4]))