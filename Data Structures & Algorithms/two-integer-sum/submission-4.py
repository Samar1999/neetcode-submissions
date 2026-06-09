class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(0, len(nums)):
            y = target - nums[i]
            if y in idx:
                return [idx[y],i]
            idx[nums[i]] = i