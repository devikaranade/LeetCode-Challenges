class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        l = 0, r = 8
        area = min(height[l], height[r])* (r-l)
        max_area = max(area, max_area)

        area = 8 max_area = 8
        l = 1, r = 8
        '''

        l = 0
        r = len(height)-1
        area = 0

        while l<=r:
            area = max(area, min(height[l], height[r])*(r-l))

            if height[l]<height[r]:
                l+=1
            else:
                r-=1 
        return area


        