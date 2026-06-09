class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        s1_mp = {}
        s2_mp = {}

        for e in s1:
            s1_mp[e] = s1_mp.get(e, 0) + 1
                 
        for r in range(len(s2)):
            s2_mp[s2[r]] = s2_mp.get(s2[r], 0) + 1
            if r - l + 1 == len(s1):
                if s2_mp == s1_mp:
                    return True
                else:
                    s2_mp[s2[l]] -= 1
                    if s2_mp[s2[l]] == 0:
                        del s2_mp[s2[l]]
                    l += 1
        return False



