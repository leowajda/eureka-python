from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.left_boundary(nums, target), self.right_boundary(nums, target)]

    @staticmethod
    def left_boundary(nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        pos = -1

        while left <= right:

            middle = (left + right) // 2

            if nums[middle] >= target:

                if nums[middle] == target:
                    pos = middle

                right = middle - 1

            else:
                left = middle + 1

        return pos

    @staticmethod
    def right_boundary(nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        pos = -1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] <= target:

                if nums[middle] == target:
                    pos = middle

                left = middle + 1

            else:
                right = middle - 1

        return pos


