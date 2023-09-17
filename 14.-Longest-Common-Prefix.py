"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""

class Solution:
    def longestCommonPrefix(self, strs:list[str]) -> str:
        longestPrefix = min(strs,key=len)
        # print(longestPrefix)
        
        while len(longestPrefix) > 0:
            print(longestPrefix)
            FLAG = False
            for i in strs:

                if longestPrefix != i:
                    if i.startswith(longestPrefix):
                        print(i,"1")
                        continue
                    else:
                        # print(i,"2")
                        FLAG =True
            if FLAG:
                longestPrefix = longestPrefix[:-1]
            else:
                print(len(longestPrefix))
                if longestPrefix:
                    # print('9')
                    return longestPrefix
                else:
                    return ""









s = Solution()
# print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))

