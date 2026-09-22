class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        val = image[sr][sc]
        if val == color:
	        return image
        row = len(image)
        col = len(image[0])
        vis = [[False for i in range(col)] for j in range(row)]
        rowdir = [1,0,0,-1]
        coldir = [0,1,-1,0]
        
        def dfs(i,j):
            vis[i][j] = True
            image[i][j] = color
            for k in range(4):
                newrow = i + rowdir[k]
                newcol = j + coldir[k]
                if 0 <= newrow < row and 0 <= newcol < col and not vis[newrow][newcol] and image[newrow][newcol] == val:
                    dfs(newrow,newcol)
        dfs(sr,sc)
        return image
