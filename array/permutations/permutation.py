class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        self.backtrack(nums, [])
        return self.res

    def backtrack(self, nums, perm):
        if not nums:
            self.res.append(perm)
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i + 1:], perm + [nums[i]])
