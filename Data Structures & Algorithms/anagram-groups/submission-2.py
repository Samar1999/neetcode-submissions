class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for e in strs:
            count = [0] * 26
            for c in e:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(e)
        return list(res.values())