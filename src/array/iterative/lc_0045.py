from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps, n = 0, len(nums)
        prev_jump = next_jump = 0

        for i in range(n - 1):
            next_jump = max(nums[i] + i, next_jump)

            if i == prev_jump:
                prev_jump = next_jump
                jumps += 1

        return jumps