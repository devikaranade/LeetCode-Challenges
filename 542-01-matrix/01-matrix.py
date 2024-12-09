class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        seen = set()
        
        directions = [(-1,0),(0,-1),(0,1),(1,0)]
        mat = [row[:] for row in mat]
        m = len(mat)
        n = len(mat[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    seen.add((i,j))

        while q:
            i,j,steps = q.popleft()
            for r,c in directions:
                nr = i+r
                nc = j+c
                if (nr,nc) not in seen and (0<=nr<m and 0<=nc<n):
                    q.append((nr,nc,steps+1))
                    seen.add((nr,nc))
                    mat[nr][nc]=steps+1
        return mat
