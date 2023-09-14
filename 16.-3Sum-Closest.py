"""Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution."""

##brute force 

## take two pointer , start and start +3 
## result to save the minimum sum
## add elements from start until start+3 if needed update result
## increment start
#3 return result

### sort the array
## take two pointers left and right\
## iterate through the array
## take sum of current element , left and right
## if sum is greater than target decrement right or else increment left
## keep writting the sum  to result if needed
class Solution:
    def threeSumClosest(self, nums: list[int],target: int) -> int:
        nums = sorted(nums)
        # print(nums)
        result = float('inf')
        n = len(nums)
        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                # print(nums[i],nums[left],nums[right])
                # print(threesum)
                if threesum == target:
                    return threesum
                elif threesum < target:
                    left += 1
                else:
                    right -= 1
                if abs(result - target) > abs(threesum-target):
                    result = threesum
                # print(result)

        if result == float('inf'):
                return 0
        return result

s = Solution()
print(s.threeSumClosest([0,0,0],1))
print(s.threeSumClosest([-1,2,1,-4],1))




