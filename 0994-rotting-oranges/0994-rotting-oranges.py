from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[False for i in range(n)] for j in range(m)]
        rowdir = [0,-1,0,1]
        coldir = [1,0,-1,0]
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    vis[i][j] = True
        count = 0
        while queue:
            length = len(queue)
            for i in range(length):
                row,col = queue.popleft()
                for j in range(4):
                    newrow = rowdir[j] + row
                    newcol = coldir[j] + col
                    if 0 <= newrow < m and 0 <= newcol < n and not vis[newrow][newcol] and grid[newrow][newcol] == 1:
                        grid[newrow][newcol] = 2
                        queue.append((newrow,newcol))
                        vis[newrow][newcol] = True
            if queue:
                count+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return count 