"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""


## technically optimal approach is two find a no solution (reverse approach)
## sort the array lexical order 
## compare the elements first str with the last 
## keep adding elements to add until there is match 
## else return ans

class Solution:
    def longestCommonPrefix(self, strs:list[str]) -> str:
        ans = ""
        strs = sorted(strs)
        # print(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return ans
            ans+=first[i]
        return ans








s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["","carrace","car"]))
print(s.longestCommonPrefix(["q","f","a"]))


