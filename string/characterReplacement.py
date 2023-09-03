"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase
English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

E.G.
    INPUT:
        s = "AABABBA", k = 1
    OUTPUT:
        Replace the one 'A' in the middle with 'B' and form "AABBBBA". The substring "BBBB" has the longest
        repeating letters, which is 4.
"""

def characterReplacement(str, k):
    ans = 0
    l = 0
    dict = {}
    for r, c in enumerate(str):
        dict[c] = 1 + dict.get(c, 0)
        while r - l + 1 - max(dict.values()) > k:
            dict[l] -= 1
            l += 1
        ans = max(ans, r - l + 1)
    return ans