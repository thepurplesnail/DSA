def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    storedS = {}
    storedT = {}

    for i in range(len(s)):
        storedS[s[i]] = storedS.get(s[i], 0) + 1

    for i in range(len(t)):
        if t[i] not in storedS:
            return False
        storedT[t[i]] = storedT.get(t[i], 0) + 1

    return storedS == storedT