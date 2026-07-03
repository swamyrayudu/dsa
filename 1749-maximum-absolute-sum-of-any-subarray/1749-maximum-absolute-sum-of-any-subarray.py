class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0] * (n+1)
        dp2 = [0] * (n+1)
        for i in range(n-1,-1,-1):
            dp1[i] = max(nums[i],nums[i]+dp1[i+1])
        for i in range(n-1,-1,-1):
            dp2[i] = min(nums[i],nums[i]+dp2[i+1])

        maxsub = float("-inf")
        minsub = float("inf")
        for i in range(n):
            maxsub = max(maxsub,dp1[i])
            minsub = min(minsub,dp2[i])
        return max(maxsub,abs(minsub))