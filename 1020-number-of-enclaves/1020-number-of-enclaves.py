from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        vis = [[False for i in range(col)] for i in range(row)]
        queue = deque()

        for i in range(row):
            if grid[i][0] == 1:
                queue.append((i,0))
                vis[i][0] = True

        for i in range(row):
            if grid[i][col-1] == 1:
                queue.append((i,col-1))
                vis[i][col-1] = True

        for i in range(col):
            if grid[0][i] == 1:
                queue.append((0,i))
                vis[0][i] = True

        for i in range(col):
            if grid[row-1][i] == 1:
                queue.append((row-1,i))
                vis[row-1][i] = True
        rowdir = [0,1,0,-1]
        coldir = [1,0,-1,0]
        while queue:
            r,c = queue.popleft()
            
            for i in range(4):
                newrow = r + rowdir[i]
                newcol = c + coldir[i]
                if 0 <= newrow < row and 0 <= newcol < col and not vis[newrow][newcol] and grid[newrow][newcol] == 1:
                    queue.append((newrow,newcol))
                    vis[newrow][newcol] = True
        count = 0
        for i in range(row):
            for j in range(col):
                if vis[i][j] != True and grid[i][j] == 1:
                    count+=1
        return count