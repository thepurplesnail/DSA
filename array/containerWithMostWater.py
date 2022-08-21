def maxArea(height: list[int]) -> int:
    l = 0
    r = len(height) - 1
    res = min(height[l], height[r]) * r
    while l < r:
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        res = max(res, min(height[l], height[r]) * (r - 1))
    return res
print(maxArea([1,8,6,2,7]))