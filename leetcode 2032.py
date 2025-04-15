''' 2032. Two Out of Three
Solved
Easy
Topics
Companies
Hint
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
 

Example 1:

Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2. '''


class Solution:
    def twoOutOfThree(self, x: List[int], y: List[int], p: List[int]) -> List[int]:
        freq = {}
        for num in set(x):
            freq[num] = freq.get(num, 0) + 1
        for num in set(y):
            freq[num] = freq.get(num, 0) + 1
        for num in set(p):
            freq[num] = freq.get(num, 0) + 1
        result = []
        for key in freq:
            if freq[key] >= 2:
                result.append(key)
        return result 
