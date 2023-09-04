"""Given a string s, find the length of the longest 
substring
 without repeating characters.
"""

## iterate through all the elements 
## check if the next element exist in previous substr if yes break the substr and store as substr
## for the next substr check if is longer than previous substr

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        longest_ss = ''
        ss = ''
        for ch in s:
            if ch not in ss:
                ss = ss+ch
                if len(ss) > len(longest_ss):
                    longest_ss = ss
            elif ch in ss:
                if len(ss) > len(longest_ss):
                    # print("ss",ss)
                    longest_ss = ss
                    ss=ch
            
        # print(longest_ss)
        return len(longest_ss)
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))         
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("c"))
print(s.lengthOfLongestSubstring("au"))



 

"""Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 """