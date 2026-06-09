class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s = list(sorted(s))
            t = list(sorted(t))
            for i in range(0, len(s)):
                if s[i] != t[i]:
                    return False
            return True
        else:
            return False