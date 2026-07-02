class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        dp1 = [-1] * (n)
        dp2 = [-1] * (n)
        def maxi(i):
            if i == n -1:
                return nums[i]
            if dp1[i] != -1:
                return dp1[i]
            dp1[i] = max(nums[i],nums[i]+maxi(i+1))
            return dp1[i]
        def mini(i):
            if i == n - 1:
                return nums[i]
            if dp2[i] != -1:
                return dp2[i]
            dp2[i] = min(nums[i],nums[i]+mini(i+1))
            return dp2[i]
        minsub = float("inf")
        maxsub = float("-inf")
        for i in range(n):
            maxsub = max(maxsub,maxi(i))
            minsub = min(minsub,mini(i))
        if maxsub < 0:
            return maxsub
        return max(maxsub,total-minsub)