class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums = set(nums)
        m = len(nums)
        if n == m:
            return False
        return True
        
    # time: O(n)
    # space: O(1)
