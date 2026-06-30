class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [-1 for i in range(n)]
        def f(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            not_pick = f(i+1)
            pick = questions[i][0] + f(i+questions[i][1]+1)
            dp[i] = max(not_pick,pick)
            return dp[i]
        return f(0)