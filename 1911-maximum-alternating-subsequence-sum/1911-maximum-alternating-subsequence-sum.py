class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for i in range(2)] for j in range(n)]
        def f(i,parity):
            if i == n:
                return 0
            if dp[i][parity] != -1:
                return dp[i][parity]
            not_pick = f(i+1,parity)
            pick = 0
            if parity == 0:
                pick = nums[i] + f(i+1,1)
            elif parity == 1:
                pick = -nums[i] + f(i+1,0)
            dp[i][parity] = max(pick,not_pick)
            return dp[i][parity]
        return f(0,0)