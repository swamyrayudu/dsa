class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n)
        def f(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            not_pick = 0 + f(i+1)
            pick = nums[i] + f(i+2)
            dp[i] = max(pick,not_pick)
            return dp[i]
        return f(0)