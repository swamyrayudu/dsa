class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxnum = max(nums)
        earn = [0] * (maxnum+1)
        for num in nums:
            earn[num] += num
        n = len(earn)
        pre1 = 0
        pre2 = 0
        for i in range(n-1,-1,-1):
            not_pick = 0 + pre1
            pick = earn[i] + pre2
            curr = max(pick,not_pick)
            pre2 = pre1
            pre1 = curr
        return pre1