class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        while l <= h:
            c = (l + h)//2
            if nums[c] == target:
                return c
            elif target > nums[c]:
                l = c + 1
            else:
                h = c - 1
        return -1