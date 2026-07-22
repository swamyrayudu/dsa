class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        next = [0] * (n+1) 
        for i in range(n-1,-1,-1):
            curr = [0] * (n+1) 
            for pre in range(i-1,-2,-1):
                not_pick = 0 + next[pre+1]
                pick = 0
                if pre == -1 or pairs[pre][1] < pairs[i][0]:
                    pick = 1 + next[i+1]
                curr[pre+1] = max(pick,not_pick)
            next = curr
        return next[0]