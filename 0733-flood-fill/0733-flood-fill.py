class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
	    original = image[sr][sc]
	    if original == color:
	        return image
	    m = len(image)
	    n = len(image[0])
	    vis = [[False for i in range(n)] for j in range(m)]
	    dfsrow = [0,1,-1,0]
	    dfscol = [1,0,0,-1]
	    def dfs(row,col):
	        vis[row][col] = True
	        image[row][col] = color
	        
	        for i in range(4):
	            newrow = dfsrow[i] + row
	            newcol = dfscol[i] + col
	            
	            if 0 <= newrow < m and 0 <= newcol < n and image[newrow][newcol] == original and not vis[newrow][newcol]:
	                dfs(newrow,newcol)
	    dfs(sr,sc)
	    return image
