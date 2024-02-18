class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid[0])):
            max_el = 0
            for j in grid:
                new_max = max(j) 
                max_el = max(max_el, new_max)
                j.remove(new_max)
            res+=max_el
        return res
