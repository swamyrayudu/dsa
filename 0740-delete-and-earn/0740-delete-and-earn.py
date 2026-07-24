class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxnum = max(nums)
        earn = [0] * (maxnum+1)
        for num in nums:
            earn[num] += num
        n = len(earn)
        dp = [-1] * (n+1)
        def f(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            not_pick = 0 + f(i+1)
            pick = earn[i] + f(i+2)
            dp[i] = max(not_pick,pick)
            return dp[i]
            
        return f(0)