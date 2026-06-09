class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # l = min(piles) 
        l = 1
        hi = max(piles) 
        ans = hi
        while l <= hi:
            k = l + (hi - l)// 2

            val = 0 # Total hrs required 
            for i in range(0, len(piles)):
                val = val + math.ceil(piles[i] / k)
            
            if val <= h:
                ans = min(k, ans)
                hi = k - 1
            elif val > h:
                l = k + 1
                
        return ans