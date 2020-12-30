"""
1566. Detect Pattern of Length M Repeated K or More Times
Easy

Given an array of positive integers arr,  find a pattern of length m that is repeated k or more times.

A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.

Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.

Example 1:

Input: arr = [1,2,4,4,4,4], m = 1, k = 3
Output: true
Explanation: The pattern (4) of length 1 is repeated 4 consecutive times. Notice that pattern can be repeated k or more times but not less.
Example 2:

Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
Output: true
Explanation: The pattern (1,2) of length 2 is repeated 2 consecutive times. Another valid pattern (2,1) is also repeated 2 times.
Example 3:

Input: arr = [1,2,1,2,1,3], m = 2, k = 3
Output: false
Explanation: The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern of length 2 that is repeated 3 or more times.
Example 4:

Input: arr = [1,2,3,1,2], m = 2, k = 2
Output: false
Explanation: Notice that the pattern (1,2) exists twice but not consecutively, so it doesn't count.
Example 5:

Input: arr = [2,2,2,2], m = 2, k = 3
Output: false
Explanation: The only pattern of length 2 is (2,2) however it's repeated only twice. Notice that we do not count overlapping repetitions.
 

Constraints:

2 <= arr.length <= 100
1 <= arr[i] <= 100
1 <= m <= 100
2 <= k <= 100
"""

from collections import defaultdict
from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        arrstr = [str(v) for v in arr]
        patterns = defaultdict(int)
        start = end = 0
        n = len(arrstr)

        while end < n:
            if (end-start)+1 > m:
                start += 1

            if (end-start)+1 == m:
                substring = ','.join(arrstr[start:end+1])
                pstart = start-m
                if pstart >= 0 and ','.join(arrstr[pstart:start]) == substring:
                    patterns[substring] += 1
                else:
                    patterns[substring] = 1
                if patterns[substring] >= k:
                    return True
            end += 1

        return False

    def containsPattern1(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        if n < m * k:
            return False

        for i in range(n - m * k + 1):
            if arr[i: i + m] * k == arr[i: i + m * k]:
                return True
        return False


if __name__ == "__main__":
    print(Solution().containsPattern(arr=[1, 2, 4, 4, 4, 4], m=1, k=3))
