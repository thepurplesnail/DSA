def gcd(x, y):
    # y is a divisor of x
    if x == 0:
        return y
    # x is a divisor of y
    if y == 0:
        return x
    # if x is greater than x -> find gcd between remainder of x divided by y & y
    if x > y:
        return gcd(x%y, y)
    else:
        return gcd(x, y%x)

print(f"gcd: {gcd(12, 36)}")

def lcm(x, y):
    return x * y/gcd(x, y)

# find gcd of an array
# [6,2,14,6]

def gcdList(arr):
    # if array is one element -> return sole element
    if len(arr) == 1:
        return arr[0]
    # iterate through array
    return gcd(arr[0], gcdList(arr[1:]))

print(f'gcdList: {gcdList([6,2,14,6])}')