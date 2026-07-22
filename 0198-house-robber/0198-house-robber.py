class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        pre1 = 0
        pre2 = 0
        for i in range(n-1,-1,-1):
            not_pick = pre1
            pick = nums[i] + pre2
            curr = max(pick,not_pick)
            pre2 = pre1
            pre1 = curr
        return pre1