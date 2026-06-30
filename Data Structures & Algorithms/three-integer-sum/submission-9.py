class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        result = set()

        for i in range(0,len(nums_sorted) - 2):

            j = i + 1
            k = len(nums_sorted) - 1

            while j < k:
                target = -(nums_sorted[i])
                int_sum = nums_sorted[j] + nums_sorted[k]
                if int_sum < target:
                    j +=1
                elif int_sum > target:
                    k -=1
                elif int_sum == target:
                    result.add((nums_sorted[i], nums_sorted[j], nums_sorted[k]))
                    j +=1
                    k -=1

        return list(result)