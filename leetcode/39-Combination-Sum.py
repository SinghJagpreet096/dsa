"""
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

## brute force 
## sort the candidate array
## start from begining 

# TODO backtracking and recursion
class Solution:
    def combinationSum(self, candidates:list[int], target:int) -> list[list[int]]:
        sol = []
        candidates.sort()
        if sum(sol) == target:
            return sol
        
        return combinationSum(candidates, target)

    
if __name__ == "__main__":
    s = Solution()
    s.combinationSum([2,3,7,6
                      ],target=7)