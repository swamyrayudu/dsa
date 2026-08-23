from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for u,v in prerequisites:
            adj[u].append(v)
            indegree[v]+=1
        queue = deque()
        count = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            count+=1
            for ner in adj[node]:
                indegree[ner]-=1
                if indegree[ner] == 0:
                    queue.append(ner)
        if count == numCourses:
            return True
        else:
            return False
