class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for e in nums:
            if e in d:
                d[e] = d[e] + 1
            else:
                d[e] = 1

        freq = [[] for i in range(len(nums) + 1)]
        for e, val in d.items():
            freq[val].append(e)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res