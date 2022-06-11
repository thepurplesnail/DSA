# 0 1 1 2 3 5
def fib(n):
    a = 0
    b = 1
    for i in range(1,n):
        temp = b
        b += a
        a = temp
    return b

print(fib(155))