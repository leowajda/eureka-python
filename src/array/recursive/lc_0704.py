from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def helper(left: int, right: int) -> int:
            if left > right:
                return -1

            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] < target:
                return helper(middle + 1, right)
            else:
                return helper(left, middle - 1)

        return helper(0, len(nums) - 1)
