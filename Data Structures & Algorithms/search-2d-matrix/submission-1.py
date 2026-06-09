class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for e in matrix:
            l = 0
            h = len(e) - 1
            while l <= h:
                if target >= e[l] and target <= e[h]:
                    m = (l + h)//2
                    if target == e[m]:
                        return True
                    elif target > e[m]:
                        l = m + 1
                    elif target < e[m]:
                        h = m - 1
                else:
                    break
        return False