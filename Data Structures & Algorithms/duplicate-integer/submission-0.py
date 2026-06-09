class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for e in nums:
            if e not in myset:
                myset.add(e)
            else:
                return True
        return False
             