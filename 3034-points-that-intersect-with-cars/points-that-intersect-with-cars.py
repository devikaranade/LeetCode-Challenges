class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        s = set()
        for i in range(len(nums)):
            first = nums[i][0]
            second = nums[i][1]
            for num in range(first,second+1):
                s.add(num)
        return len(s)
                

            