class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) - 1
        potential = -1
        while l <= r:
            mid = l + (r - l)//2

            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid]) - 1]:
                potential = mid
                break
            elif target > matrix[mid][0]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
                
        if potential == -1:
            return False
        
        l = 0
        r = len(matrix[potential]) - 1

        while l <= r:
            mid = l + (r - l)//2

            if target == matrix[potential][mid]:
                return True
            elif target > matrix[potential][mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
            