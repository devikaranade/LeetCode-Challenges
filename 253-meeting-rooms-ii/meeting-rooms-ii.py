class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        rooms = 0

        starts = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        e = 0
        for i in range(len(starts)):
            if starts[i]>=end[e]:
                e+=1
            else:
                rooms+=1
        return rooms

