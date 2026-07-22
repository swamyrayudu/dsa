class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        pre1 = 0
        pre2 = 0
        for i in range(n-1,-1,-1):
            one_step = float('inf')
            if i+1 <= n:
                one_step = cost[i] + pre1
            two_step = float('inf')
            if i + 2 <= n:
                two_step = cost[i] + pre2
            pre2 = pre1
            curr = min(one_step,two_step)  
            pre1 =curr
        return min(pre1,pre2)      
    