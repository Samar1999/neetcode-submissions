class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:

            mid = low + (high - low)//2

            if nums[mid] <= nums[high]:
                if target >= nums[mid] and target <= nums[high]:
                    if target == nums[mid]:
                        return mid
                    elif target > nums[mid]:
                        low = mid + 1
                    elif target < nums[mid]:
                        high = mid - 1
                else:
                    high = mid - 1
            else:
                if target <= nums[mid] and target >= nums[low]:
                    if target == nums[mid]:
                        return mid
                    elif target > nums[mid]:
                        low = mid + 1
                    elif target < nums[mid]:
                        high = mid - 1
                else:
                    low = mid + 1
        return -1