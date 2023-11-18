"""


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if len(stack)==0 or not self.isMatching(stack[len(stack)-1],c):
                    return False
                else:
                    stack.pop()
        return len(stack)==0
    
    def isMatching(self, open:chr, close:chr) -> bool:

        return (open == "(" and close == ")") or (open == "{" and close == "}") or (open == "[" and close == "]")
            

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("["))

