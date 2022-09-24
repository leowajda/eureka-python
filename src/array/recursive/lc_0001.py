from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        def helper(pos: int) -> List[int]:
            complement = target - nums[pos]
            if complement in map:
                return [pos, map[complement]]
            map[nums[pos]] = pos

            return helper(pos + 1)

        return helper(0)
