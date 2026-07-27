class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[False for i in range(n)] for j in range(m)]

        def dfs(row,col):
            vis[row][col] = True

            dfsrow = [1,0,0,-1]
            dfscol = [0,1,-1,0]
            for i in range(4):
                newrow = row + dfsrow[i]
                newcol = col + dfscol[i]
                if 0 <= newrow < m and 0 <= newcol < n and grid[newrow][newcol] == '1' and not vis[newrow][newcol]:
                    dfs(newrow,newcol)

        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1' and not vis[row][col]:
                    count+=1
                    dfs(row,col)
        return count
        