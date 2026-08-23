from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for u,v in prerequisites:
            adj[u].append(v)
            indegree[v]+=1
        queue = deque()
        stack = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            stack.append(node)
            for ner in adj[node]:
                indegree[ner]-=1
                if indegree[ner] == 0:
                    queue.append(ner)
        if len(stack) == numCourses:
            return stack[::-1]
        else:
            return []        