class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = max(nums)
        earn = [0] * (max_num+1)
        for num in nums:
            earn[num] += num
        dp = [-1 for i in range(max_num+1)]
        def f(i):
            if i < 0:
                return 0
            if i == 0:
                return earn[0]
            if dp[i] != -1:
                return dp[i]
            not_pick = f(i-1)
            pick = earn[i] + f(i-2)
            dp[i] = max(not_pick,pick)
            return dp[i]
        return f(max_num)