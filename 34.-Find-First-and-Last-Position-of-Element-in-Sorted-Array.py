

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
                    if start < 1 and end >= n-1:

                        return [start,end]
                    if nums[start-1] == target and start > 0:
                        # print('start',start)
                        start -= 1
                    elif end <= n-2 and nums[end+1] == target:
                        # print('end',end)
                        end += 1
                    else:
                        return [start,end]
                # print("1")
                
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return res
    
s = Solution()
# print(s.searchRange(nums=[5,7,7,8,8,10],target=8))
# print(s.searchRange(nums=[5,7,7,8,8,10],target=6))
# print(s.searchRange(nums=[],target=0))
print(s.searchRange(nums=[1],target=1))
print(s.searchRange(nums=[2,2],target=2))
print(s.searchRange(nums=[0,0,0,1,2,3],target=0))






