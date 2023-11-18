class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combined  = nums1 + nums2
        combined.sort()
        print(combined)
        n = len(combined)
        median = n//2
        if n%2==0:
            return (combined[median] + combined[median-1])/2
        return combined[median]

            
        

s = Solution()
print(s.findMedianSortedArrays([1,3], nums2 = [2]))
print(s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))

