class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = [[-1 for i in range(n)] for j in range(n+1)]
        def f(i,pre):
            if i == n:
                return 0
            if dp[i][pre] != -1:
                return dp[i][pre]
            not_pick = 0 + f(i+1,pre)
            pick = 0
            if pre == -1 or pairs[pre][1] < pairs[i][0]:
                pick = 1 + f(i+1,i)
            dp[i][pre] = max(pick,not_pick)
            return dp[i][pre]
        return f(0,-1)