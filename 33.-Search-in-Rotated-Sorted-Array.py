"""

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 

return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


"""


## for the rotated array, the array is still sorted in two parts
## we have to just figure out which part does the target belongs to and apply binary search on that , more of a divide and conquer

class Solution:
    def search(self, nums: list[int], target:int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            
            mid = (left+right)//2
            # print(nums[mid],mid)
            if nums[mid] == target:
                return mid
            elif (nums[left] < nums[mid] and target >= nums[left] and target < nums[mid]) or \
                (nums[left] > nums[mid] and( target < nums[mid] or target >= nums[left]) ):
                right = mid-1
            else:
                left = mid + 1

        return -1
    
if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2],target=0))
    print(s.search([4,5,6,7,0,1,2],target=3))
    print(s.search([4,5,6,7,0,1,2],target=5))
    print(s.search([1,2,3,4,5,6],target=4))


