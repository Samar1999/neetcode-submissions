class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_prof = [0] * len(nums)
        left_prof[0] = 1

        right_prod = [0] * len(nums)
        right_prod[len(nums) - 1] = 1

        for l in range(1, len(nums)):
            left_prof[l] = left_prof[l - 1] * nums[l - 1]

        for r in range(len(nums) - 2, -1, -1):
            right_prod[r] = right_prod[r + 1] * nums[r + 1]
        
        res = []
        for i in range(0, len(nums)):
            res.append(left_prof[i] * right_prod[i])
        
        return res