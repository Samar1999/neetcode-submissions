class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            h = len(nums) - 1
            while l < h:
                s = nums[i] + nums[l] + nums[h]
                if s == 0:
                    res.append([nums[i], nums[l], nums[h]])
                    h -=1
                    l +=1
                    while l < h and nums[l-1] == nums[l]:
                        l += 1
                    while l < h and nums[h+1] == nums[h]:
                        h -=1
                elif s > 0:
                    h -=1
                else:
                    l +=1
        return res