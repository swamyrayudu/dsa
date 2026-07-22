class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+2)
        for i in range(n-1,-1,-1):
            not_pick = dp[i+1]
            pick = nums[i] + dp[i+2]
            dp[i] = max(pick,not_pick)
        return dp[0]