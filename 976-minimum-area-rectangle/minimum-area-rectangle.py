class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float('inf')
        vis = set()
        for x,y in points:
            for xv,yv in vis:
                if (xv,y) in vis and (x,yv) in vis:
                    area = abs(xv-x)*abs(yv-y)
                    res = min(res,area)
            vis.add((x,y))
        return res if res!=float('inf') else 0