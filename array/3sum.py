'''
MEDIUM
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]


'''
def threeSum(nums: list[int]) -> list[list[int]]:
    ans = []
    nums.sort()
    for i in range(len(nums)):
        # if current num not equal to previous -> do 2sum on subarray after current index
        if i == 0 or nums[i] != nums[i - 1]:
            # left and right pointer
            l, r = i + 1, len(nums) - 1
            # while pointers haven't crossed
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                # if 3sum < 0 -> move left pointer 1 right
                if total < 0:
                    l += 1
                # if 3Sum > 0 -> move right pointer 1 left
                elif total > 0:
                    r -= 1
                # 3Sum = 0 -> add [current, left, right] to ans
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    # -> move left pointer to the right until it's value is different from the last
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
    return ans
print(threeSum([-1,0,1,2,-1,-4]))