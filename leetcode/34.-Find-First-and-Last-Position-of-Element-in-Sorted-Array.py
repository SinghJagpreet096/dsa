

class Solution:
    def searchRange(self, nums: list[int], target:int) -> list[int]:
        n = len(nums)
        left = 0
        right = n-1
        res = [-1,-1]
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                # print('mid',mid)
                start = mid
                end = mid
                while True:
                    
                    if nums[start] != target or start <= 1:
                        break
                    else:
                        start -= 1
                    if nums[end] != target or end >= n-2:
                        break
                    else:
                        end += 1
                return [start,end]

                
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return res
    
s = Solution()
print(s.searchRange(nums=[5,7,7,8,8,10],target=8))
print(s.searchRange(nums=[5,7,7,8,8,10],target=6))
print(s.searchRange(nums=[],target=0))
print(s.searchRange(nums=[1],target=1))
print(s.searchRange(nums=[2,2],target=2))
print(s.searchRange(nums=[0,0,0,1,2,3],target=0))






