class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(nums) - 1):
            print(nums[i])
            for e in range(i + 1, len(nums)):
                print(nums[e])
                if nums[i] + nums[e] == target:
                    result.append(i)
                    result.append(e)
                    return result
                    break           