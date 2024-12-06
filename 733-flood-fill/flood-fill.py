class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_pixel = image[sr][sc]
        if original_pixel == color:
            return image
        else:
            image[sr][sc]=color
        m = len(image)
        n = len(image[0])
        q = deque([(sr,sc)])
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
    
        while q:
            row, col = q.popleft()
            for r,c in directions:
                nr = r + row
                nc = c + col
                if 0<=nr<m and 0<=nc<n and image[nr][nc]==original_pixel:  
                    q.append((nr,nc))
                    image[nr][nc]=color
        return image
