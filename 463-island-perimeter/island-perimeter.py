class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    p+=4
                    if col>0 and grid[row][col-1]==1:
                        p-=2
                    if row>0 and grid[row-1][col]==1:
                        p-=2
        return p