from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_min = local_min = float('inf')
        global_max = local_max = float('-inf')

        prefix_sum = 0
        for num in nums:
            local_min = min(num, num + local_min)
            local_max = max(num, num + local_max)

            global_min = min(global_min, local_min)
            global_max = max(global_max, local_max)

            prefix_sum += num

        return global_max if global_max < 0 else max(global_max, prefix_sum - global_min)