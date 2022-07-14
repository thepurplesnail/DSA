'''
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such
that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or
-1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

E.g.          [6,7,0,1,2,4,5]
Input: nums = [4,5,6,7,0,1,2] target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    m = (l + r) // 2

    while l <= r:
        mid = nums[m]
        left = nums[l]
        right = nums[r]

        if mid == target:
            return m

        # if middle element is less than left, middle is in the right sorted array
        if mid < left:
            # if target's value is between middle and right's -> search for target right of middle
            if mid < target <= right:
                l = m + 1
            # else: look for target left of middle
            else:
                r = m - 1
        # else middle is in the left sorted array
        else:
            # if target's value is between left and middle -> search for target left of middle
            if left <= target < mid:
                r = m - 1
            # else look for target right of middle
            else:
                l = m + 1
        m = (l + r) // 2
    return -1
