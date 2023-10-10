"""


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(1,len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    # print(s[i],"()")
                    continue
                else:return False
            if s[i] == "]":
                if s[i-1] == "[":
                    # print(s[i],"[]")
                    continue
                else:
                    return False
            if s[i] == "}":
                if s[i-1] == "{":
                    # print(s[i],"{}")
                    continue
                else:
                    return False

        return True
                


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
