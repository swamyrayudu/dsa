class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxi = 0
        m = len(accounts)
        n = len(accounts[0])
        for row in range(m):
            sumi = 0
            for col in range(n):
                sumi+=accounts[row][col]
            if sumi > maxi:
                maxi = sumi
        return maxi