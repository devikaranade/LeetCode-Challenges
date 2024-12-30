class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        q = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def bfs(i,j):
            q.append((i,j))

            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    nr = row+dr
                    nc = col+dc

                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]=="1":
                        q.append((nr,nc))
                        grid[nr][nc]="0"        

        for row in range(m):
            for col in range(n):
                if grid[row][col]=="1":
                    bfs(row, col)
                    count+=1
        return count
        