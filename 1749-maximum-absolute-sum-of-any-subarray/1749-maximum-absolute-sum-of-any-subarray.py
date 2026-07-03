class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        pre1 = 0
        pre2 = 0
        maxsub = float("-inf")
        minsub = float("inf")
        for i in range(n-1,-1,-1):
            curr = max(nums[i],nums[i]+pre1)
            curr2 = min(nums[i],nums[i]+pre2)
            maxsub = max(maxsub,curr)
            minsub = min(minsub,curr2)
            pre1 = curr
            pre2 = curr2

        return max(maxsub,abs(minsub))