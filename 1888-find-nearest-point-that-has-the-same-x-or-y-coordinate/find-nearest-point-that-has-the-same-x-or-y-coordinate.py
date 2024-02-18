class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minval = 99999
        idx = -1
        for point in range(len(points)):
            x1 = points[point][0]
            y1 = points[point][1]
            if x1==x or y1==y:
                dist = abs(x1-x) + abs(y1-y)
                if dist<minval:
                    minval=dist
                    idx = point
        return idx
             
        