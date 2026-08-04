class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        vis = [[False for i in range(col)] for i in range(row)]
        rowdir = [0,1,-1,0]
        coldir = [1,0,0,-1]
        def dfs(r,c):
            vis[r][c] = True
            for i in range(4):
                newrow = r + rowdir[i]
                newcol = c + coldir[i]
                if 0 <= newrow < row and 0 <= newcol < col and not vis[newrow][newcol] and board[newrow][newcol] == 'O':
                    dfs(newrow,newcol)
        for i in range(row):
            if board[i][0] == 'O':
                dfs(i,0)
        for i in range(row):
            if board[i][col-1] == 'O':
                dfs(i,col-1)
        for i in range(col):
            if board[0][i] == 'O':
                dfs(0,i)
        for i in range(col):
            if board[row-1][i] == 'O':
                dfs(row-1,i)
        
        for i in range(row):
            for j in range(col):
                if vis[i][j] != True:
                    board[i][j] = 'X'
        