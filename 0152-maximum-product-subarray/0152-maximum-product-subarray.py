class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n)
        def f(i):
            if i == n - 1:
                return (nums[i],nums[i])
            if dp[i] != -1:
                return dp[i]
            nextmax,nextmin = f(i+1)

            maxproduct = max(nums[i],
                            nums[i]*nextmax,
                            nums[i]*nextmin)

            minproduct = min(nums[i],
                            nums[i]*nextmax,
                            nums[i]*nextmin)
            dp[i] = (maxproduct,minproduct)
            return dp[i]
        ans = float("-inf")
        for i in range(n):
            maxproduct,minproduct = f(i)
            ans = max(ans,maxproduct)
        return ans