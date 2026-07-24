class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxnum = max(nums)
        earn = [0] * (maxnum+1)
        for num in nums:
            earn[num] += num
        n = len(earn)
        dp = [0] * (n+2)
        for i in range(n-1,-1,-1):
            not_pick = 0 + dp[i+1]
            pick = earn[i] + dp[i+2]
            dp[i] = max(pick,not_pick)
        return dp[0]