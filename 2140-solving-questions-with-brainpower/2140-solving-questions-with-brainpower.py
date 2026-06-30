class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)
        for i in range(n-1,-1,-1):
            not_pick = dp[i+1]
            next_ind = i + questions[i][1] + 1
            pick = questions[i][0]
            if next_ind <= n:
                pick+=dp[next_ind]
            dp[i] = max(pick,not_pick)
        return dp[0]