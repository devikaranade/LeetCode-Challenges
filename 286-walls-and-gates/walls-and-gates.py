class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        walls, gate, room = -1, 0, 2147483647
        directions = [(-1,0),(0,-1),(0,1),(1,0)]

        queue=deque()
        
        max_row = len(rooms)
        max_col = len(rooms[0])

        for r in range(max_row):
            for c in range(max_col):
                if rooms[r][c]==0:
                    queue.append((r,c))
        dist = 1
        while queue:
            n = len(queue)
            for _ in range(n):
                row,col = queue.popleft()
                for nr,nc in directions:
                    new_row = row+nr
                    new_col = col+nc
                    if new_row<0 or new_row>=max_row or new_col<0 or new_col>=max_col or rooms[new_row][new_col]!=room:
                        continue
                    rooms[new_row][new_col] = dist
                    queue.append((new_row,new_col))
            dist+=1

        
        

                
            
            
        
        