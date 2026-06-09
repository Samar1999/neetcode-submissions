class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        h = len(heights) - 1
        MaxArea = 0
        while l < h:
            val = min(heights[l], heights[h]) * (h - l)
            MaxArea = max(val, MaxArea)
            if heights[l] > heights[h]:
                h -=1
            else:
                l +=1
        return MaxArea
            
