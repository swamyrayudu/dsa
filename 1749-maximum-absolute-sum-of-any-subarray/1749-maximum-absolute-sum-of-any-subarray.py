class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
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
            if i == n -1:
                return nums[i]
            if dp2[i] != -1:
                return dp2[i]
            dp2[i] = min(nums[i],nums[i]+mini(i+1))
            return dp2[i]

        maxsub = float("-inf")
        minsub = float("inf")
        for i in range(n):
            maxsub = max(maxsub,maxi(i))
            minsub = min(minsub,mini(i))
        return max(maxsub,abs(minsub))