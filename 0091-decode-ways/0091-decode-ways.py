class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * (n)
        def f(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]
            one_digit = f(i+1)
            two_digit = 0
            if i+1 < n and 10<=int(s[i:i+2])<= 26:
                two_digit = f(i+2)
            dp[i] = one_digit+two_digit
            return dp[i]
        return f(0)