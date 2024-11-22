class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = heights[-1]
        result = [len(heights)-1]
        for r in range(len(heights)-2,-1,-1):
            if heights[r]>max_height:
                max_height = heights[r]
                result.append(r)
        return result[::-1]
