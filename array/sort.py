def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    L = nums[:mid]
    R = nums[mid:]
    mergeSort(L)
    mergeSort(R)
    merge(L, R, nums)
    return nums

def merge(L, R, nums):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1
    # when L or R are unequal lengths
    while i < len(L):
        nums[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        nums[k] = R[j]
        j += 1
        k += 1

print(mergeSort([5,1,3,5,2,3]))