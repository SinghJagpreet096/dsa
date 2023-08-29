"""You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

"""


class Solution:
    def bestClosingTime(self, customers:str) -> int:
        # print(" ")
        min_penalty = 106
        close_hour = 0
        # if 'N' not in customers:
        #     return len(customers)
        for i in range(len(customers)):
            penalty = 0
            for j in range(len(customers)):
                if j < i:
                    if customers[j]=='N':
                        penalty+=1
                elif j >= i:
                    if customers[j]=='Y':
                        penalty+=1
            if penalty < min_penalty:
                min_penalty = penalty
                close_hour = i

        if close_hour == len(customers)-1:
            return len(customers)
    
s = Solution()
print(f"Input:'YYNY'\n Output:{s.bestClosingTime('YYNY')}")

print(f"Input:'NNNNN'\n Output:{s.bestClosingTime('NNNNN')}")

print(f"Input:'YYYY'\n Output:{s.bestClosingTime('YYYY')}")

        




"""Example 1:

Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
Example 2:

Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.
Example 3:

Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.
 

Constraints:

1 <= customers.length <= 105
customers consists only of characters 'Y' and 'N'.
        """