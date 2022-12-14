from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        b, a = nums[-1], 0

        for i in range(n - 2, -1, -1):
            a, b = b, max(b, a + nums[i])

        return max(a, b)