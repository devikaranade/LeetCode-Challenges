class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        length_paths = [[-1] * n for _ in range(m)]

        def rec(i: int,j: int,prev: int)-> int:
            if i<0 or j<0 or i>=m or j>=n or prev>=matrix[i][j]:
                return 0
            if length_paths[i][j]==-1:
                length_paths[i][j]=max(rec(i,j-1,matrix[i][j]),
                rec(i,j+1,matrix[i][j]),
                rec(i-1,j,matrix[i][j]),
                rec(i+1,j,matrix[i][j])
                )
            return length_paths[i][j]+1
        gen = (rec(i,j,-1) for i in range(m) for j in range(n))
        return max(gen)

    