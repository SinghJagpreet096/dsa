""""Given an array nums of n integers, 
return an array of 
all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:"""

## brute force 
## create all combination of 4 elements of arra
## check if the position each element is unique2 are unique and sum == target
## timecomplexity : O(n**4)

class Solution:
    def fourSum(self, nums:list[int], target: int) -> list[list[int]]:
        result = set()
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                for k in range(j+1,n-1):
                    for l in range(k+1,n):
                        if (i != j and j!= k and k!=l) :
                            if nums[i] + nums[j] + nums[k] + nums[l] == target:
                                result.add(tuple(sorted([nums[i],nums[j],nums[k],nums[l]])))
                                   
           
        return [list(res) for res in result]
    
s = Solution()
print(s.fourSum([1,0,-1,0,-2,2],0))
print(s.fourSum([-5,5,4,-3,0,0,4,-2],4))





