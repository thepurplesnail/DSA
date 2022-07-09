def containsDuplicate(nums: list[int]) -> bool:
    stored = set()
    for n in nums:
        if n in stored:
            return True
        else:
            stored.add(n)
    return False
print(containsDuplicate([1,2,3,1]))