class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        vis = [False] * V
        path = [0] * V
        ans = []
        def dfs(i):
            vis[i] = True
            path[i] = 1
            
            for ner in graph[i]:
                if not vis[ner]:
                    if dfs(ner):
                        return True
                elif path[ner] == 1:
                    return True
            path[i] = 0
            return False
            
        for i in range(V):
            if not vis[i]:
                dfs(i)
        
        for i in range(V):
            if path[i] == 0:
                ans.append(i)
        return ans