class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        d = {}
        for i, interval in enumerate(intervals):
            d[interval[0]]=i
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        res = [-1]*len(intervals)

        for i, interval in enumerate(intervals):
            idx = bisect_left(sorted_intervals, [interval[1] , -float('inf')])
            if idx!=len(intervals):
                res[i]=d[sorted_intervals[idx][0]]
        return res