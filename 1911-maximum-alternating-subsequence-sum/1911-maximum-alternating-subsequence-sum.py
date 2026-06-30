class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for i in range(2)] for j in range(n+1)]

        for i in range(n-1,-1,-1):
            for parity in range(2):
                not_pick = dp[i+1][parity]
                pick = 0
                if parity == 0:
                    pick = nums[i] + dp[i+1][1]
                else:
                    pick = -nums[i] + dp[i+1][0]
                dp[i][parity] = max(not_pick,pick)
        return dp[0][0]