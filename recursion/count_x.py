def count(s):
    # if s has 0 characters -> return 0
    if len(s) == 0:
        return 0
    last = len(s) - 1
    # if character at last index of s is equal to x -> increment output
    if s[last] == 'x':
        return 1 + count(s[0: last])
    # else remove the last character of s
    else:
        return count(s[0: last])

print(count("1x41x"))