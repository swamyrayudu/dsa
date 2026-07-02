class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n)
        def f(i):
            if i == n -1:
                return nums[i]
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(nums[i],nums[i]+f(i+1))
            return dp[i]
        ans = float("-inf")
        for i in range(n):
            ans = max(ans,f(i))
        return ans