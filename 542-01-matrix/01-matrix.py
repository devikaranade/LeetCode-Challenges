class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    queue.append((i,j))
                else:
                    mat[i][j]="#"

        while queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    dr = i+dx
                    dc = j+dy
                    if 0<=dr<m and 0<=dc<n and mat[dr][dc]=="#":
                        mat[dr][dc]=mat[i][j]+1
                        queue.append((dr,dc))
        return mat
                
                
                
            

        