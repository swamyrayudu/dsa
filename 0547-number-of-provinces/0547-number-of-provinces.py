from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        vis = [False] * V

        def bfs(node):
            vis[node] = True
            queue = deque()
            queue.append(node)
            vis[node] = True
            while queue:
                node = queue.popleft()
                
                for ner in range(V):
                    if isConnected[node][ner] == 1 and not vis[ner]:
                        queue.append(ner)
                        vis[ner] = True
                        
        count = 0
        for i in range(V):
            if not vis[i]:
                count+=1
                bfs(i)
        return count
