class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for e in strs:
            l = "".join(sorted(e))
            if l in res.keys():
                res[l].append(e)
            else:
                res.setdefault(l, []).append(e)
        final = list(res.values())
        return final
