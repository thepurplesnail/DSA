'''
MEDIUM
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

Input: nums = [-2,2,3,0,2,4]
               -4|2
                  -12|6
                     1|1
                       2|2
                         8|8
Output: 8
Explanation: [2,4] has the largest product 8.
'''
def maxProduct(nums):
    ans = currMin = currMax = nums[0]
    for n in nums[1:]:
        if n == 0:
            # reset current min and max to 1
            currMin = currMax = 1
            # set ans to 0 in case 0 is the largest product so far
            ans = max(ans, n)
        else:
            x = currMin * n
            y = currMax * n
            currMin = min(n, x, y)
            currMax = max(n, x, y)
            # update ans appropriately
            ans = max(ans, currMax)
    return ans

print(maxProduct([2,3,-2,4]))