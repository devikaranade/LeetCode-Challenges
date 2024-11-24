class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        count = 0
        m = len(grid)
        n = len(grid[0])
        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            while queue:
                row, col = queue.popleft()
                for dr,dc in directions:
                    r,c = row+dr, col+dc
                    if 0<=r<m and 0<=c<n and grid[r][c]=="1":   
                        queue.append((r,c))
                        grid[r][c]="0"


        
    
        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    bfs(r,c)
                    count+=1
        return count
                
        
        
        