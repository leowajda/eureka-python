class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        memo, encodings = [0] * (n + 1), set([str(i) for i in range(1, 27)])
        memo[n] = 1

        for i in range(n - 1, -1, -1):
            if s[i:i + 1] in encodings:
                memo[i] = memo[i + 1]

            if i + 2 <= n and s[i: i + 2] in encodings:
                memo[i] += memo[i + 2]

        return memo[0]
