class Solution:
    def divide(self, dividend:int, divisor:int) -> int:
        quotient = 0
        upper_bound = 2**31-1
        lower_bound = -2**31
        NEG = False
        if divisor < 0 and dividend < 0:
            NEG = False
        elif divisor < 0 or dividend < 0:
            NEG = True
        dividend,divisor = abs(dividend),abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            quotient +=1
        if NEG:
            quotient = -quotient

        return lower_bound if quotient < lower_bound else quotient if quotient < 0 else upper_bound if quotient > upper_bound else quotient
    
s = Solution()
print(s.divide(10,3))
print(s.divide(7,-3))
