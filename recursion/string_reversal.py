def reverse(s):
    if len(s) == 1:
        return s
    last = len(s) - 1
    return s[last] + reverse(s[:last])


print(reverse("hello"))