class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}

        def trib(n):
            if n not in memo:
                memo[n] = trib(n - 1) + trib(n - 2) + trib(n - 3)
            return memo[n]

        return trib(n)