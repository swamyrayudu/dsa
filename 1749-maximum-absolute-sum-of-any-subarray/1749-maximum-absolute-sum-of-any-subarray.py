class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        pre1 = 0
        maxsub = float("-inf")
        for i in range(n-1,-1,-1):
            curr = max(nums[i],nums[i]+pre1)
            maxsub = max(maxsub,curr)
            pre1 = curr
        minsub = float("inf")
        pre2 = 0
        for i in range(n-1,-1,-1):
            curr = min(nums[i],nums[i]+pre2)
            minsub = min(minsub,curr)
            pre2 = curr

        return max(maxsub,abs(minsub))