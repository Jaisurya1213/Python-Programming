'''Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false'''

'''Rotated sorted array '''

class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        arr.sort()
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
                break
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            return False
