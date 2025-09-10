class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        q = deque()
        for i in range(m):
            if board[i][0]=='O':
                q.append((i,0))
            if board[i][n-1]=='O':
                q.append((i, n-1))

        for j in range(n):
            if board[0][j]=='O':
                q.append((0,j))
            if board[m-1][j]=='O':
                q.append((m-1,j))
            
        dir_= [(0,1),(1,0),(0,-1),(-1,0)]
        while q:
            x,y = q.popleft()
            if 0<=x<m and 0<=y<n and board[x][y]=='O':
                board[x][y]='S'
                for dx,dy in dir_:
                    q.append((x+dx,y+dy))
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='S':
                    board[i][j]='O'

