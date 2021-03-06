"""
1201. Ugly Number III
Medium

Given four integers n, a, b, and c, return the nth ugly number.

Ugly numbers are positive integers that are divisible by a, b, or c.

Example 1:

Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
Example 4:

Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984
 

Constraints:

1 <= n, a, b, c <= 109
1 <= a * b * c <= 1018
It is guaranteed that the result will be in range [1, 2 * 109].
"""
from itertools import gcd
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        #least common mutiple 
        ab = a*b//gcd(a, b)
        bc = b*c//gcd(b, c)
        ca = c*a//gcd(c, a)
        abc = ab*c//gcd(ab, c)
        
        def fn(k):
            """Return the number of ugly numbers less than or equal to k"""
            return k//a + k//b + k//c - k//ab - k//bc - k//ca + k//abc
        
        #binary search to find the lowest k such that fn(k) >= n
        lo, hi = 0, 2_000_000_000
        while lo < hi:
            mid = (lo + hi)//2
            if fn(mid) >= n: hi = mid
            else: lo = mid + 1
        return lo