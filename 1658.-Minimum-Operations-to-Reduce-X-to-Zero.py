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
        target = sum(nums) - x
        max_len = 0
        left = 0
        n = len(nums)
        cur_sum = 0
        if target == 0:
            return n
        for right,val in enumerate(nums):
            cur_sum += val
            while left <=right and cur_sum > target:
                cur_sum -= nums[left]
                left +=1
            if cur_sum == target:
                max_len = max(max_len,right-left+1)
            

        return n - max_len if max_len else -1
                

s = Solution()
print(s.minOperations([3,2,20,1,1,3], x = 10))