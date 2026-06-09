class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx = []
        for i in range(0, len(numbers) - 1):
                for j in range(i+1, len(numbers)):
                    if numbers[i] + numbers[j] == target:
                        idx.append(i+1)
                        idx.append(j+1)
                        break
        return idx

