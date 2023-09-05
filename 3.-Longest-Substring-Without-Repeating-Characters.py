"""Given a string s, find the length of the longest 
substring
 without repeating characters.
"""

## iterate through all the elements 
## check if the next element exist in previous substr if yes break the substr and store as substr
## for the next substr check if is longer than previous substr


## optimal solution with two pointers and set
## take left and right pointer as boundaries of substr
## iterate the str with right pointer
## keep storing the char in charSet until no repeated char and update the maxlength if needed
## if char is repeated in the set remove all char from charSet using left pointer until the right pointer
## do the same for remaining str
## return maxlength

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        maxLength = 0
        charSet = set()
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        return maxLength
        
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))         
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("c"))
print(s.lengthOfLongestSubstring("aab"))



 

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