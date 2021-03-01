"""
560. Subarray Sum Equals K
Medium

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k. 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:    
        count, total, cache = 0, 0, { 0: 1 }
        
        for val in nums:
            total += val
            if total - k in cache: 
                count += cache[total - k]
            cache[total] = (cache[total] if total in cache else 0) + 1
        
        return count
        