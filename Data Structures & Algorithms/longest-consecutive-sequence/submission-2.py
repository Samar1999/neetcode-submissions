class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {e: False for e in nums}
        longestLength = 0

        for e in nums:
            c = 1
            
            nextnum = e + 1
            while (nextnum in d) and d[nextnum] == False:
                c += 1
                d[nextnum] = True
                nextnum +=1
            
            prevnum = e - 1
            while (prevnum in d) and d[prevnum] == False:
                c += 1
                d[prevnum] = True
                prevnum -=1
            
            longestLength = max(c, longestLength)

        return longestLength


            