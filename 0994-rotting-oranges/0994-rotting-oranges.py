from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        count0s = 0
        count1s = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    count0s += 1
                elif grid[row][col] == 1:
                    count1s += 1
                else:
                    queue.append([row,col])
        if count1s == 0:
            return 0
        bfsrow = [0,1,-1,0]
        bfscol = [1,0,0,-1]
        count = 0
        while queue:
            change = False
            for i in range(len(queue)):
                node = queue.popleft()
                for i in range(4):
                    newrow = bfsrow[i] + node[0]
                    newcol = bfscol[i] + node[1]
                    if 0 <= newrow < m and 0 <= newcol < n and grid[newrow][newcol] == 1:
                        queue.append([newrow,newcol])
                        grid[newrow][newcol] = 2
                        count1s-=1
                        change = True
            if change:
                count+=1
        if count1s > 0:
            return -1
        return count
