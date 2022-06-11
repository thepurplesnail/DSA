def sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr.pop() + sum(arr)


print(sum([1,2,3,4]))

