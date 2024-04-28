class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        minutes = fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        q.append((-1,-1))
        minutes = -1
        dir_ = [(-1,0),(0,1),(1,0),(0,-1)]
        while q:
            row, col = q.popleft()
            if row==-1:
                minutes+=1
                if q:
                    q.append((-1,-1))
            else:
                for d in dir_:
                    nr,nc=row+d[0],col+d[1]
                    if 0<=nr<m and 0<=nc<n:
                        if grid[nr][nc]==1:
                            grid[nr][nc]=2
                            fresh-=1
                            q.append((nr,nc))
        return minutes if fresh==0 else -1

        