"""Given a signed 32-bit integer x, return x with its digits reversed.
 If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""

## brute force --> beats 96% 

## result stores the reversed no
## NEG is flag to indicate if there is negative input(default False)

## check if the no is negative change the NEG flag to True and write x with absolute value
## take the last element by using modulus and save write it to result and multiple the existing result value with 10 to send it to the next tenth place
## and divide x with 10 until x>9 i.e x reached single digit
## write x to result as last element is missed in the while loop
# check if the original no was neg add minus sign
## check if the result is between int32 range if yes return 0
# else return result
#  



class Solution:
    def reverse(self, x:int) -> int:
        result = 0
        NEG = False
        if x < 0:
            NEG = True
            x = abs(x)
        while (x)>9:
            result = result*10 + (x%10)
            x=x//10
        # print("res",result*10+x)
        result = result*10 + x
        if NEG: 
            result = -result
        if result > 2**31 or result < -2**31-1:
            return 0
        else:
            return result
            

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))




"""
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1"""