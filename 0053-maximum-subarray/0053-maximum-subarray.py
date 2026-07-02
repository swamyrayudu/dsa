class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        for i in range(n-1,-1,-1):
            dp[i] = max(nums[i],nums[i]+dp[i+1])

        ans = float("-inf")
        for i in range(n):
            ans = max(ans,dp[i])
        return ans