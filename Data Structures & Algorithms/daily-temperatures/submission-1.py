class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        indx = [len(temperatures) - 1]
        for i in range(len(temperatures)-2, -1, -1):
            while len(indx) > 0 and temperatures[i] >= temperatures[(indx[-1])]:
                indx.pop()
            if len(indx) == 0:
                res[i] = 0
            else:
                res[i] = indx[-1] - i
            indx.append(i)
        return res

                