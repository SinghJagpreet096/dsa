"""Given a string s, return the longest palindromicsubstring in s."""


##using two pointers
## use left and right pointers
## 1.check the substr is palindrome if True break and return substr
## decrement right by 1 and check 1 else increment left and check 1
## else increment left by 1 and decrement right 1 
## repeat until left <= right


## optimal solutions
## palindrome consist of a center and similar elements  on the left and right of center, 
## as long the left and right of the center are equal we keep increasing the substr
## we iterate through the string considering each element as center
## and call expand function which returns palindrome str by expanding the elements around center if elements are similar
## for edge case if two elements are same ("bb") we call expand on i,i+1
## we keep writting to longestSubstr if new substr in greater than the existing one




class Solution:
    def longestPalindrome(self, s:str) -> str:
        longestSubstr = ''
        for i in range(len(s)):
            longestSubstr = max(longestSubstr, expand(s,i,i), expand(s,i,i+1), key=len)
        return longestSubstr

def expand(s,i,j) -> str:
    while i>=0 and j<len(s) and s[i]==s[j]:
        i -=1
        j +=1
    return s[i+1:j]

s = Solution()
print(s.longestPalindrome('babad'))
print(s.longestPalindrome('bb'))
print(s.longestPalindrome('cbbd'))





"""Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
