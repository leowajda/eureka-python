from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            middle = (left + right) // 2

            if middle + 1 == len(nums) or nums[middle] > nums[middle + 1]:
                result = middle
                right = middle - 1
            else:
                left = middle + 1

        return result
