class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        p=image[sr][sc]
        if p==color:
            return image
        else:
            image[sr][sc]=color
        
        m = len(image)
        n = len(image[0])
        q = deque([(sr,sc)])
        dir_ = [(-1,0), (0,-1),(1,0), (0,1)]
        while q:
            r,c = q.popleft()
            for i,j in dir_:
                nr = i+r
                nc = j+c
                if 0<=nr<m and 0<=nc<n and image[nr][nc]==p:
                    q.append((nr,nc))
                    image[nr][nc]=color
                
        return image

