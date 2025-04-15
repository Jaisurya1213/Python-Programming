''' 2085. Count Common Words With One Occurrence
Solved
Easy
Topics
Companies
Hint
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

 

Example 1:

Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.'''

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq1 = {}
        for i in words1:
            if i not in freq1:
                freq1[i]=1
            else:
                freq1[i] += 1
        freq2 ={}
        for i in words2:
            if i not in freq2:
                freq2[i]=1
            else:
                freq2[i] += 1
        count = 0
        for word in freq1:
            if word in freq2 and freq1[word] == 1 and freq2[word] == 1:
                count += 1
        return count
