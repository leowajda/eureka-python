from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        for i in range(n, 2 * n):
            nums[i - n] |= (nums[i] << 10)

        ones = int(pow(2, 10)) - 1
        for i in range(n - 1, -1, -1):
            a, b = (nums[i] & ones), (nums[i] >> 10)
            nums[2 * i] = a
            nums[2 * i + 1] = b

        return nums