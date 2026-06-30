class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        # left = [0] * n
        right = [0] * n
        left = 0

        for i in range(1, n):
            # left[i] = max(left[i-1], height[i-1])
            right[(n-1) - i] = max(right[(n-1) - i + 1], height[(n-1) - i + 1])
        
        total_water = 0
        for i in range(0, n):
            if(i>0): left = max(left, height[i-1])
            water_above_me = max(min(left, right[i]) - height[i], 0)
            total_water = total_water + water_above_me

        return total_water
        
