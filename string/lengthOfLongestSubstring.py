"""
Given a string s, find the length of the longest substring without repeating characters.

E.G.:
    INPUT:
        s = "abcabcbb"
    OUTPUT:
        3
    EXPLANATION:
        "abc" is length 3

    INPUT:
        s = "pwwkew"
    OUTPUT:
        3
    EXPLANATION:
        "wke" is length 3
"""

def lengthOfLongestSubstring(s):
    if len(s) < 2:
        return len(s)

    stored = {}
    ans = 0
    l = 0
    for r, c in enumerate(s):
        if c in stored:
            l = max(l, stored[c] + 1)
        stored[c] = r
        ans = max(ans, r - l + 1)

    return ans