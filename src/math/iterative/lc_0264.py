class Solution:
    def nthUglyNumber(self, n):

        factors, k = [2, 3, 5], 3
        positions, nums = [0] * k, [1]

        for i in range(n - 1):
            ugly_nums = [factors[j] * nums[positions[j]] for j in range(k)]
            min_ugly = min(ugly_nums)
            nums.append(min_ugly)
            positions = [positions[j] + (ugly_nums[j] == min_ugly) for j in range(k)]

        return nums[-1]
