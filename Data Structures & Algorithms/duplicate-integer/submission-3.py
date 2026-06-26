class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        sorted_arry = sorted(nums)

        for i in range(1,len(sorted_arry)):
            if sorted_arry[i] == sorted_arry[i - 1]:
                return True
                
        return False