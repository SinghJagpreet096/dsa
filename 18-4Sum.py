""""Given an array nums of n integers, 
return an array of 
all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:"""

## brute force 
## create all combination of 4 elements of arra
## check if the position each element is unique2 are unique and sum == target
## timecomplexity : O(n**4)

# 

class Solution:
    def fourSum(self, nums:list[int],target:int) -> list[list[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                lo = j+1
                hi = n-1
                while lo < hi:
                    # print(i,j,lo,hi)
                    temp = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if temp == target:
                        res.append([nums[i],nums[j],nums[lo],nums[hi]])
                        while lo < hi and nums[lo]==nums[lo+1]:
                            lo += 1
                        lo += 1
                        while lo<hi and nums[hi]==nums[hi-1]:
                            hi -= 1
                        hi -= 1
                    elif temp < target:
                        lo += 1
                    else:
                        hi -= 1
        return res
                
s = Solution()
print(s.fourSum([1,0,-1,0,-2,2],0))
print(s.fourSum([-5,5,4,-3,0,0,4,-2],4))





