class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def f(i,dp):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            one_step = float('inf')
            if i+1 <= n:
                one_step = cost[i] + f(i+1,dp)
            two_step = float('inf')
            if i + 2 <= n:
                two_step = cost[i] + f(i+2,dp)
            dp[i] = min(one_step,two_step)
            return dp[i]
        ans = float('inf')
        dp = [-1] * n
        for i in range(2):
            ans = min(ans,f(i,dp))
            dp = [-1] * n
        return ans