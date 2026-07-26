from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        vis = [False] * (V) 
            
        def dfs(node):
            vis[node] = True

            for ner in range(len(isConnected)):
                if isConnected[node][ner] == 1 and not vis[ner]:
                    dfs(ner)
        count = 0
        for i in range(V):
            if not vis[i]:
                count+=1
                dfs(i)
        return count
