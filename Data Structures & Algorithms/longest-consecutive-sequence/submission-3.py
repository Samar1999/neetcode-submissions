class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Hash Map for visited elements
        v_map = {}
        for e in nums:
            v_map[e] = False

        res = 0
        for e in nums:
            
            max_count = 1
            next_num = e + 1
            # To find next element in hash map
            while next_num in v_map and v_map[next_num] == False:
                max_count += 1
                v_map[next_num] = True
                next_num += 1
            
            prev_num = e - 1
            # To find previous element in hash map
            while prev_num in v_map and v_map[prev_num] == False:
                max_count += 1
                v_map[prev_num] = True
                prev_num -= 1
            
            res = max(res, max_count)
        
        return res