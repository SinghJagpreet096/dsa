"""You are given an integer array nums and an integer x. 
In one operation, you can either remove the leftmost or the rightmost element from the array nums and 
subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

"""

## brute force 

## take two pointers 
## check if element at last or first is less than x 
## and check which is bigger between first and last
## substract the no from x and count the steps

class Solution:
    def minOperations(self, nums:list[int],x:int) -> int:
        left = 0
        right = len(nums)-1
        count = 0

        while left < right:
            if x == nums[left] or x == nums[right]:
                return count + 1

            if nums[left] < x and nums[right] < x:
                x = x - max(nums[left],nums[right])
                count += 1
                if nums[left] > nums[right]:
                    left += 1 
                else:
                    right -= 1

            elif nums[left] < x:
                x = x - nums[left]
                left += 1
                count += 1

            else:
                x = x - nums[right]
                right -= 1
                count += 1
        return -1


s = Solution()
print(s.minOpererations([3,2,20,1,1,3], x = 10))