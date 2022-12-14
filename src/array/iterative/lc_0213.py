from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[-1]

        def helper(start: int, end: int) -> int:
            nonlocal n, nums

            b, a = nums[end], 0
            for i in range(end - 1, start - 1, -1):
                a, b = b, max(a + nums[i], b)

            return max(a, b)

        return max(helper(0, n - 2), helper(1, n - 1))
