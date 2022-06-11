def palindrome(s):
    # if s is one character or empty string -> return true
    if len(s) == 1 or len(s) == 0:
        return True
    last = len(s) - 1
    # if characters at ends of s are not equal -> return false
    if s[0] != s[last]:
        return False
    # perform function on substring
    return palindrome(s[1:last])
