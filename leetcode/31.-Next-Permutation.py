## brute force
## check if i is less than i + 1 if yes increment i 
## when we find element out of order we sort the remaing elements


class Solution:
    def nextPermutation(self, nums:list[int]) -> None:
        i = 0
        while i < len(nums)-1:
            if nums[i] < nums[i+1]:
                i += 1
            else:
                break
        nums[i:len(nums)].sort()
        print(nums)
        return nums


s = Solution()
s.nextPermutation([2,3,1])