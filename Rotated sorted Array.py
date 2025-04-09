''' Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1     

Rotated Sorted Array'''


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l=0
        r=len(arr)-1
        while l<=r:
            m=(l+r)//2
            if arr[m]==target:
                return m
            if arr[l] <= arr[m]:
                if arr[l]<= target < arr[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if arr[m]< target <= arr[r]:
                    l = m+1
                else:
                    r = m-1
        return -1
