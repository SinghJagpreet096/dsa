"""Given a string s, return the longest palindromicsubstring in s."""


##brute force
## create all possible substr and find the max substr which is palindrome



class Solution:
    def longestPalindrome(self, s:str) -> str:
        longestSubstr = ''
        if len(s)==1:
            return s
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    substr=s[i:j+1]
                else:
                    substr = s[i:j]
                if substr == substr[-1::-1]:
                    # print(substr)
                    if len(substr) > len(longestSubstr):
                        longestSubstr = substr
        return longestSubstr
        
                

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
