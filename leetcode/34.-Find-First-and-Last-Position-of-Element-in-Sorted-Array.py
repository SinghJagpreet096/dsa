

# class Solution:
#     def searchRange(self, nums: list[int], target:int) -> list[int]:
#         n = len(nums)
#         left = 0
#         right = n-1
#         res = [-1,-1]
#         while left <= right:
#             mid = (left+right)//2
#             if nums[mid] == target:
#                 # print('mid',mid)
#                 start = mid
#                 end = mid
#                 while True:
                    
#                     if nums[start] != target or start <= 1:
#                         break
#                     else:
#                         start -= 1
#                     if nums[end] != target or end >= n-2:
#                         break
#                     else:
#                         end += 1
#                 return [start,end]

                
#             elif nums[mid] > target:
#                 right = mid-1
#             else:
#                 left = mid+1
#         return res
    
s = Solution()
print(s.searchRange(nums=[5,7,7,8,8,10],target=8))
print(s.searchRange(nums=[5,7,7,8,8,10],target=6))
print(s.searchRange(nums=[],target=0))
print(s.searchRange(nums=[1],target=1))
print(s.searchRange(nums=[2,2],target=2))
print(s.searchRange(nums=[0,0,0,1,2,3],target=0))


def binarySearch(lo, hi, condition):
    while lo <= hi:
        mid = (lo+hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        else:
            lo = mid+1
    return -1

def firstPosition(nums: list[int], target:int)->int:
    def condition(mid):
        if nums[mid] == target:
            if mid-1 >=0 and nums[mid-1] == target:
                return 'left'
            else:
                return 'found'
        elif nums[mid] > target:
            return 'left'
        else:
            return 'right'
            
        
    return binarySearch(0,len(nums)-1,condition)
def lastPosition(nums:list[int],target:int)->int:
    def condition(mid):
        if nums[mid] == target:
            if mid+1 < len(nums) and nums[mid+1] == target:
                return 'right'
            else:
                return 'found'
        elif nums[mid] > target:
            return 'left'
        else:
            return 'right'

    return binarySearch(0, len(nums)-1, condition)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [firstPosition(nums, target), lastPosition(nums, target)]




