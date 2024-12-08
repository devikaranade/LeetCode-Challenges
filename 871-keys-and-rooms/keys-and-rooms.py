class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        count = 0
        n = len(rooms)-1
        q = deque([rooms[0]])
        visited = set()
        visited.add(0)
        while q:
            room = q.popleft()
            for i in room:
                if i not in visited:
                    q.append(rooms[i])
                    visited.add(i)
        if len(rooms)==len(visited):
            return True
        return False
