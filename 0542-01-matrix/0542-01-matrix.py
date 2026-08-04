from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
	    V = len(mat)
	    row = len(mat)
	    col = len(mat[0])
	    vis = [[False for i in range(len(mat[0]))] for i in range(len(mat))]
	    dis = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
	    queue = deque()
	    rowdir = [0,1,-1,0]
	    coldir = [1,0,0,-1]
	    for i in range(row):
	        for j in range(col):
	            if mat[i][j] == 0:
	                vis[i][j] = True
	                queue.append([i,j,0])
	    while queue:
	        node = queue.popleft()
	        dis[node[0]][node[1]] = node[2]
	        for i in range(4):
	            newrow = node[0] + rowdir[i]
	            newcol = node[1] + coldir[i]
	            
	            if 0 <= newrow < row and 0 <= newcol < col and not vis[newrow][newcol]:
	                dis[newrow][newcol] = node[2] + 1
	                queue.append([newrow,newcol,node[2]+1])
	                vis[newrow][newcol] = True
	    return dis
	            