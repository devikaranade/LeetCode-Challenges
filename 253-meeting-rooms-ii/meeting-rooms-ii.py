class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        min_heap = []
        rooms = 0
        intervals.sort()
        for interval in intervals:
            if min_heap==[] or min_heap[0]>interval[0]:
                heapq.heappush(min_heap, interval[1])
            else:
                heapq.heapreplace(min_heap, interval[1])
        return len(min_heap)
