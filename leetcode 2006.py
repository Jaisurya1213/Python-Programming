'''2006. Count Number of Pairs With Absolute Difference K
Solved
Easy
Topics
Companies
Hint
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0. '''


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        if k < 0:  
            return 0
        count = 0
        num_map = {}
        for num in nums:
            if num - k in num_map:
                count += num_map[num - k]
            if num + k in num_map:
                count += num_map[num + k]
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1
        return count
