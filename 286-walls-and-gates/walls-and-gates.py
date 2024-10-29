class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gate , obstacle, empty_room = 0, -1, 2147483647

        m = len(rooms)
        n = len(rooms[0])

        queue = collections.deque([])
        empty_rooms = set()

        for i in range(m):
            for j in range(n):
                if rooms[i][j]==gate:
                    queue.append((i,j,0))
                    empty_rooms.add((i,j))
                if rooms[i][j]==empty_room:
                    empty_rooms.add((i,j))
        while queue:
            x,y, distance = queue.popleft()
            if (x,y) in empty_rooms:
                rooms[x][y]=distance
                empty_rooms.remove((x,y))

                queue.append((x+1,y,distance+1))
                queue.append((x-1,y,distance+1))
                queue.append((x,y+1,distance+1))
                queue.append((x,y-1,distance+1))