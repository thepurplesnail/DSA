"""
write a function that returns an array of all anagrams of a
given string. An anagram is a reordering of all the characters within a string.
For example, the anagrams of "abc" are:
["abc",
"acb",
"bac",
"bca",
"cab",
"cba"]
"""

def anagrams(s):
    if len(s) == 1:
        return s
    ans = []
    # find all anagrams of the substring of s 1st character onwards
    subset = anagrams(s[1:])

    # iterate through each anagram in subset
    for i in range(len(subset)):
        anagram = subset[i]
        # insert first character of s into anagram from the 1st index to after the last
        for j in range(len(anagram) + 1):
            ans.append(anagram[:j] + s[0] + anagram[j:])

    return ans


print(anagrams("abc"))
