"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. 
Read this character in if it is either. This determines if the final result is negative or positive respectively. 
Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result."""



## brute force

## use the ord function to convert each char to ASCII value, substract it with ZERO ('ASCII value 48') which gives us our result.


class Solution:
    def myAtoi(self, s:str) -> int:
        START = False
        zero = ord('0')
        negative = 0
        positive = 0

        
        # print(ord('0'),ord('9'))
        result = 0
        ## remove preceding spaces
        s = s.strip()

        
        ## negative or positive
        # if s.startswith('-'):
        #     # print("a")
        #     NEG = True
        #     s = s[1:]
        #     # print(s)
        # if s.startswith("+"):
        #     s = s[1:]
        for ch in s:
            if ch=='-' and START==False:
                negative +=1
                continue
            if ch=='+' and START==False:
                positive += 1
                continue
            
            # print(ch, START)
            ch = ord(ch)
            
            START=True
            
            # print(ch)
            if ch >= 48 and ch <=57 and START:
        
                result = result*10 + (ch - zero)
            else:
                break
        # print(positive,negative)
        if (negative > 0 and positive) > 0 or positive>1 or negative>1:
            return 0
        if negative > 0:
            # print('res',result)
            result = -result if -result > -(2**31) else -2**31
        else:
            result = result if result <= (2**31)-1 else 2**31-1
        
        
        return result
            
        
        
        

        


s = Solution()
print(s.myAtoi('     -123'))
print(s.myAtoi('42'))
print(s.myAtoi('-42'))
print(s.myAtoi('4193 with words'))

print(s.myAtoi("21474836460"))
print(s.myAtoi("00000-42a1234"))
print(s.myAtoi(' --1'))


