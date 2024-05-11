class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        @lru_cache(maxsize=None)
        def dfs(i,j):
            if obstacleGrid[i][j]:
                return 0
            if i==r-1 and j==c-1:
                return 1
            count=0
            if i<r-1:
                count+=dfs(i+1,j)
            if j<c-1:
                count+=dfs(i,j+1)
            return count
        return dfs(0,0)