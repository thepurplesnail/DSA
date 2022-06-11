def doubleArr(arr, index, arr2):
    if index == len(arr):
        return arr2
    arr2.append(2 * arr[index])
    return doubleArr(arr, index + 1, arr2)


ans = doubleArr([1,2,3,4], 0, [])
print(ans)

