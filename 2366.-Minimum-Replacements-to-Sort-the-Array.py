"""You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order."""




## find the no out of order
## we want to split the no such that the first part is <= element before it and second part is <= the first part.
## brute force would be iterate through the array and find the element that is out of order and then split it.
## and count the no of splits.

class Solution:
    def minimumReplacement(self, nums:list[int]) -> int:
        n = len(nums)
        last = nums[n-1]
        count = 0

        ## traverse reverse
        for i in range(n-2,-1,-1):
            # print(f"last:{last},nums[i]:{nums[i]}")
            if nums[i] > last:

                t = nums[i]//last ## No. of times number to be divided to equal last
                # print(f"t:{t}")
                if nums[i]%last: ## if does not divide completly add one to t
                    t+=1
                last = nums[i]//t ## update last with numsn divide by t
                print(last)
                count += t-1
            else:
                last = nums[i]
        return count 



                
s= Solution()
print(s.minimumReplacement(nums=[3,9,3]))

print(s.minimumReplacement(nums=[1,2,3,4,5]))

print(s.minimumReplacement(nums=[2,10,20,19,1]))

## time complexity : O(n)
## space complexity: O(1)
        

"""
Example 1:

Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.

Example 2:

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: The array is already in non-decreasing order. Therefore, we return 0. 
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109"""