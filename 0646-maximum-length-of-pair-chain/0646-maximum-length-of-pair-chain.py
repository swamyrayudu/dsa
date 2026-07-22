class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(n-1,-1,-1):
            for pre in range(i-1,-2,-1):
                not_pick = 0 + dp[i+1][pre+1]
                pick = 0
                if pre == -1 or pairs[pre][1] < pairs[i][0]:
                    pick = 1 + dp[i+1][i+1]
                dp[i][pre+1] = max(pick,not_pick)
        return dp[0][0]