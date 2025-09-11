class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(row,col):
            return 0<=row<m and 0<=col<n
    
        q = deque()
        dir_ = [(0,1),(1,0),(-1,0),(0,-1)]
        mat = [row[:] for row in mat]
        m = len(mat)
        n = len(mat[0])
        seen = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    seen.add((i,j))

        
        while q:
            r,c,step = q.popleft()
            for dr,dc in dir_:
                nr = r+dr
                nc = c+dc
                if (nr,nc) not in seen and valid(nr,nc):
                    seen.add((nr,nc))
                    q.append((nr,nc,step+1))
                    mat[nr][nc]=step+1
        return mat
