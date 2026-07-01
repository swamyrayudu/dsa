class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1] * (n+1)
        def f(i):
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            if dp[i] != -1:
                return dp[i]
            first = f(i-1)
            second = f(i-2)
            third = f(i-3)
            dp[i] = first+second+third
            return dp[i]
        return f(n)