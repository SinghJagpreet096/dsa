"""Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space."""


## brute force 

## sort the array
## iterate the array and find if no is equal to next no.

## optimal solution
## define a set uni which keep track of all unique values and if element is aleardy in set return element


class Solution:
    def findDuplicate(self, nums:list[int]) -> int:
        uni = set()
        for i in nums:
            if i in uni:
                return i
            else:
                uni.add(i)
            

s = Solution()
print(s.findDuplicate([1,3,4,2,2]))
print(s.findDuplicate([3,1,3,4,2]))

