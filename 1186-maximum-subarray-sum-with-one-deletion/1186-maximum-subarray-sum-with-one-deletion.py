class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[-1 for i in range(2)] for i in range(n)]
        def f(i,delone):
            if i >= n:
                return float("-inf")
            if i == n-1:
                return arr[i]
            if dp[i][delone] != -1:
                return dp[i][delone]
            if delone == 0:
                pick = arr[i] + f(i+1,0)
                delete = f(i+1,1)
                new_st = arr[i]
                dp[i][delone] = max(pick,delete,new_st)
                return dp[i][delone]
            else:
                pick = arr[i] + f(i+1,1)
                new_st = arr[i]
                dp[i][delone] = max(pick,new_st)
                return dp[i][delone]

        ans = float("-inf")
        for i in range(n):
            ans = max(ans,f(i,0))
        return ans