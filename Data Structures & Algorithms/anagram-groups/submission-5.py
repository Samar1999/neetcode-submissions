class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = defaultdict(list)
        
        for word in strs:
            counter = [0]*26
            
            for s in word:
                counter[ord(s) - ord('a')] = counter[ord(s) - ord('a')] + 1
            
            dict1[tuple(counter)].append(word)

        return list(dict1.values())

        
                
            
            

