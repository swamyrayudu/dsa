class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * 2
        for i in range(n-1,-1,-1):
            curr = [0] * 2
            for parity in range(2):
                not_pick = pre[parity]
                pick = 0
                if parity == 0:
                    pick = nums[i] + pre[1]
                else:
                    pick = -nums[i] + pre[0]
                curr[parity] = max(not_pick,pick)
            pre = curr
        return pre[0]