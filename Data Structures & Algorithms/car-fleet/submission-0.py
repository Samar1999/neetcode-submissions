class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed))
        res = []
        for i in range(len(pairs)-1, -1, -1):
            val = 0
            val = (target - (pairs[i][0]))/(pairs[i][1])
            if len(res) == 0:
                res.append(val)
            elif val > res[-1]:
                res.append(val)
        return len(res)

