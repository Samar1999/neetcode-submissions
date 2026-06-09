class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(0, len(numbers)):
            complement = target - numbers[i]
            if complement in idx:
                return [idx[complement],int(i+1)]
                break
            idx[numbers[i]] = int(i + 1)
            
                

